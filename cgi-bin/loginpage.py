#!/usr/bin/python3
import cgi,cgitb


print("")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <!-- css -->
    <link rel="stylesheet" href="/css/index.css">
</head>
<body>
    <div class="login-box">
        <h2>Login</h2>
        <form id="login" method="post" action="/cgi-bin/login">
            <!-- username -->
            <div class="user-box">
                <input type="text" name="Uname" required="" id="Uname">
                <label for="">Username</label>
            </div>

            <!-- password -->
            <div class="user-box">
                <input type="password" name="Pass" required="" id="Pass">

                <label for="">Password</label>
            </div>
            <!--token-->
            <input name="token" value="645454514251425" hidden>

            <!-- sumbit and register -->
            <div class="flex">

                <div class="button-from " id="submit">
                    <input type="submit" name="submitprompt" value="Login">
                </div>
                <div id="register">
                    Don't have an account ?
                    <a href="/cgi-bin/regpage">Register</a>
                </div>

            </div>

        </form>
    </div>
</body>
</html>
""")