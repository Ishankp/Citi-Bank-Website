const API_BASE = "http://127.0.0.1:8000";

async function apiRequest(path, options = {}) {
  const response = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json" },
    ...options,
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
