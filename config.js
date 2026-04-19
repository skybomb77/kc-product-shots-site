const CONFIG = {
    api: "https://interstaminal-unvirtuously-gennie.ngrok-free.dev/comicforge",
    auth_api: "http://localhost:5010",
    name: "SnapForge",
    version: "1.0.0"
};
if (location.hostname === 'localhost' || location.hostname === '127.0.0.1') {
    CONFIG.api = 'http://localhost:5000';
    CONFIG.auth_api = 'http://localhost:5010';
}
