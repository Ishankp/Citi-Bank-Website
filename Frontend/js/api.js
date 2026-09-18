const API_BASE = "";

async function apiRequest(path, options = {}) {
  const session = getSession();
  const headers = { "Content-Type": "application/json", ...options.headers };
  if (session && session.access_token) {
    headers.Authorization = `Bearer ${session.access_token}`;
  }

  const response = await fetch(`${API_BASE}${path}`, {
    ...options,
    headers,
  });

  if (!response.ok) {
    let detail = `Request failed (${response.status})`;
    try {
      const body = await response.json();
      detail = body.detail || detail;
    } catch {
      // ignore body parse errors
    }
    throw new Error(detail);
  }

  if (response.status === 204) {
    return null;
  }

  return response.json();
}

function getQueryParam(name) {
  return new URLSearchParams(window.location.search).get(name);
}

function formatDate(isoString) {
  return new Date(isoString).toLocaleString();
}

const SESSION_KEY = "citibank_session";

function setSession(accessToken, user) {
  sessionStorage.setItem(SESSION_KEY, JSON.stringify({ access_token: accessToken, ...user }));
}

function getSession() {
  const raw = sessionStorage.getItem(SESSION_KEY);
  return raw ? JSON.parse(raw) : null;
}

function clearSession() {
  sessionStorage.removeItem(SESSION_KEY);
}

function requireSession() {
  const user = getSession();
  if (!user) {
    window.location.href = "../login.html";
    return null;
  }
  return user;
}
