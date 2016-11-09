/* This example will only work in the latest browsers */
const initApp = () => {
  const registryToken = "6cccf66a-ea01-42af-a92c-31891a692618";

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

