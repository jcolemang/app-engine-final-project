/* This example will only work in the latest browsers */
const initApp = () => {
  const registryToken = "291f57e6-b86a-404e-834b-f62c17f3e764";

  const login = () => {
    Rosefire.signIn(registryToken, (err, rfUser) => {
      if (err) {
        return;
      }
      window.location.replace('/login?token=' + rfUser.token);
    });
  };
  const loginButton = document.getElementById('login');
  if (loginButton) {
    loginButton.onclick = login;
  }
}

window.onload = initApp;

