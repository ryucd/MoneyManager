<html lang="en">
  <head>
	<title>{{title}}</title>
    <meta name="google-signin-scope" content="profile email">
    <meta name="google-signin-client_id" content="{{GOOGLE_CLIENT_ID}}">
    <script src="https://apis.google.com/js/platform.js" async defer></script>
  </head>
  <body>
    <div class="g-signin2" data-onsuccess="onSignIn" data-theme="dark"></div>
    <script>
      function onSignIn(googleUser) {
        // Useful data for your client-side scripts:
        var profile = googleUser.getBasicProfile();
        console.log("ID: " + profile.getId()); // Don't send this directly to your server!
        console.log("Name: " + profile.getName());
        console.log("Image URL: " + profile.getImageUrl());
        console.log("Email: " + profile.getEmail());

        // The ID token you need to pass to your backend:
        var id_token = googleUser.getAuthResponse().id_token;
        console.log("ID Token: " + id_token);

		var xhr = new XMLHttpRequest();
		xhr.open('POST', '{{SERVER_URL}}/tokensignin');
		xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
		xhr.onload = function() {
			console.log('Signed in as: ' + xhr.responseText);
		};
		xhr.send('idtoken='+id_token);
      };
    </script>
  </body>
</html>
