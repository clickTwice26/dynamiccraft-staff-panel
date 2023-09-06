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
    print(f"""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DynamicCraft</title>
    <link rel="stylesheet" href="/css/global.css">
           
    <link rel="shortcut icon" href="/images/dynamiccraft-logo.png" type="image/x-icon">
    <link rel="stylesheet" href="/css/fonts.css">
</head>
<body>
    <div class="topbar">
<p style="font-family: 'hi';">Staff Panel</p>
<a id="log-out" href="#">Log Out</a>
<a class="user-info" href="#">{username}</a>
<img src="/images/default-user-img.png" alt="dynamiccraft-logo">
<!-- <div class="hide">Hi, My name is admin</div> -->

<a href="index.html">Home</a>
<a href="#">Performance</a>
<a href="documents.html">Documents</a>
<a href="#">Contact Admin</a>
<a class="active" href="reportbug.html">Report A Bug</a>

    </div>
    <div class="currentStatus">
        <h3>Current Status <span id="currentonline">{currentstatus}</span> </h3>
    </div>
    <div class="mainBOX">
        <div class="attendenceBOX">
            <div class="aS-title">
              <h4 >Attendence Box</h4>
            </div>
            <div class="aS-box">
                <form action="/cgi-bin/userpanel.py2" method="post" class="atform">
                   <hr>
                    <div class="radio-toolbar">
                        <input type="radio" id="radioApple" name="status" value="start" {currentStatus}>
                        <label for="radioApple">Start</label>
                    
                        <input type="radio" id="radioBanana" name="status" value="end">
                        <label for="radioBanana">End</label>

                    </div>
                    <input type="text" name="uname" value="{username}" hidden>
                    <input type="text" name="token" value="{token}" hidden>
                  <input id='btn-submit' type="submit" value="Submit">
                    
                </form>
            </div>
        </div>
        <div class="activitydetails">
            <h4>Activity Dashboard</h4>
        <hr>
       <ul>
        <li class="subdetails">Current Status: Online</li>
        <li class="subdetails">Last Start: time</li>
        <li class="subdetails">Last End: time</li>
        <li class="subdetails">Total today time: time</li>
       </ul>
        </div>
    </div>
    <div class="log">
        <p class="logs"> _>Log1</p>
        <p class="logs"></p>
        <p class="logs"></p>
        <p class="logs"></p>
        <p class="logs"></p>
    </div>
    <div class="footer">
    <p>All Rights Reserved</p></div>
</body>
</html>



""")
