<?php


function read_contact(){

    $api_url = 'https://site.com/api/v1/read_contact';

    $contact_id=565;// contact_id

    $organization_id=750;// organization_id

    $data = array(
        'contact_id' => $contact_id, 
        'organization_id'=> $organization_id,
        );



    $headers = array('Authorization: Bearer TOKEN',
    'Accept' => 'application/json',
    );



    // Create a cURL handle

    $ch = curl_init();



    // Set the cURL options

    curl_setopt($ch, CURLOPT_URL, $api_url);

    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

    curl_setopt($ch, CURLOPT_POST, true);

    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));

    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    

    // Execute the cURL request

    $response = curl_exec($ch);

    curl_close($ch);



    // Parse the JSON response

    $contactData = json_decode($response, true);

    echo"<pre>";

    print_r($contactData);

    var_dump($contactData);


 }
 
 read_contact();