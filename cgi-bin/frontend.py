def login(token):
    print("")
    print(f"""
<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>Simple Login Form Example</title>
  <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Rubik:400,700'><link rel="stylesheet" href="/style.css">

</head>
<body>
<!-- partial:index.partial.html -->
<div class="login-form">
  <form action="/cgi-bin/userpanel.py" method="POST">
    <h1>Login</h1>
    <div class="content">
      <div class="input-field">
        <input name="uname" type="text" placeholder="Username" autocomplete="nope">
      </div>
      <div class="input-field">
        <input name="passw" type="password" placeholder="Password" autocomplete="new-password">
      </div>
          <input type="text" name="token" value="{token}" hidden>
      <a href="#" class="link">Forgot Your Password?</a>
    </div>
    <div class="action">
      
      <button>Sign in</button>
    </div>
  </form>
</div>
<!-- partial -->
  <script  src="/script.js"></script>

</body>
</html>



""")

def staffpanel(username, token, password):
    pass
