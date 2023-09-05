<?php

$utente = 'USER';
$password = 'PSW';

$wsdl_url = 'https://example.com?wsdl';

$client = new SoapClient($wsdl_url, array('trace' => 1));

$params = array(
    'userName' => $utente,
    'password' => $password
);

try {
    
    $token_response = $client->getToken(array('USERNAME' => $utente, 'PASSWORD' => $password));

    $token = $token_response->getTokenResult;
    
    echo "Token:" . $token;
} catch (SoapFault $e) {
 
    echo "Errore: " . $e->getMessage();
}

?>
