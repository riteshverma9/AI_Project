const chatWindow = document.getElementById("chat-window");
const chatForm = document.getElementById("chat-form");
const chatInput = document.getElementById("chat-input");

function appendLine(role, text, pending) {
  const wrapper = document.createElement("div");
  wrapper.className = `line ${role}`;

  const promptSpan = document.createElement("span");
  promptSpan.className = "prompt";
  promptSpan.textContent = role === "user" ? "$" : ">";

  const textSpan = document.createElement("span");
  textSpan.className = pending ? "text pending" : "text";
  textSpan.textContent = text;

  wrapper.appendChild(promptSpan);
  wrapper.appendChild(textSpan);
  chatWindow.appendChild(wrapper);
  chatWindow.scrollTop = chatWindow.scrollHeight;
  return textSpan;
}

async function sendMessage(message) {
  const response = await fetch("/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });

  if (!response.ok) {
    const errorBody = await response.json().catch(() => ({}));
    throw new Error(errorBody.detail || "request failed");
  }

  const data = await response.json();
  return data.reply;
}

chatForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const message = chatInput.value.trim();
  if (!message) return;

  appendLine("user", message, false);
  chatInput.value = "";
  chatInput.disabled = true;
  const submitButton = chatForm.querySelector("button");
  submitButton.disabled = true;

  const pending = appendLine("assistant", "thinking", true);

  try {
    const reply = await sendMessage(message);
    pending.textContent = reply;
    pending.classList.remove("pending");
  } catch (err) {
    pending.textContent = `error: ${err.message}`;
    pending.classList.remove("pending");
  } finally {
    chatInput.disabled = false;
    submitButton.disabled = false;
    chatInput.focus();
  }
});

chatInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    chatForm.requestSubmit();
  }
});