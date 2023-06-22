<?php
    function redirect(){
      $query = http_build_query([
        'client_id' => 'CLIENT_ID', // Put client id
        'redirect_uri' => 'MYSITE.URL', // Redirect url
        'response_type' => 'code',
        'scope' => '',
        'state' => 'done',
    ]);
    return redirect('https://TARGET-SITE.com/oauth/authorize?'.$query);
    }
    
    function generate_token(){
        $tokenUrl = 'https://TARGET-SITE.com/oauth/token'; // Token url
        // Set the token request parameters
        $data = array(
            'grant_type' => 'authorization_code', // The type of token being requested
            'client_id' => 'CLIENT_ID', // Your client ID
            'client_secret' => 'CLIENT_SECRET', // Your client secret
            'redirect_uri' => 'https://MYSITE.URL/generate_token', // Redirect url
            'code' => $_GET['code'],
        );

        // Create a cURL handle
        $ch = curl_init();

        // Set the cURL options
        curl_setopt($ch, CURLOPT_URL, $tokenUrl);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    
        // Execute the cURL request
        $response = curl_exec($ch);

        // Close the cURL handle
        curl_close($ch);

        // Parse the JSON response
        $tokenData = json_decode($response, true);
        echo"<pre>";
        print_r($tokenData);

        // Access the token from the response
        if (isset($tokenData['access_token'])) {
            $accessToken = $tokenData['access_token'];
            echo 'Access Token is: ' . $accessToken;
        } else {
            echo 'Error: Failed to obtain access token';
        }
    }
