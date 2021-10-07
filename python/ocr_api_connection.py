import requests as req
import json

api_key = "api_key"   #get yours at https://us11.list-manage.com/subscribe?u=ce17e59f5b68a2fd3542801fd&id=252aee70a1


def ocr_local(filename, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with local file.
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = req.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def ocr_url(url, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with remote file.
    :param url: Image url.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = req.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()
  
  
#use example (local file)

test_local = ocr_local(filename="test.png", api_key=api_key)
dictionary = json.loads(test_local)
result = dictionary["ParsedResults"][0]["ParsedText"]
result


#use example (online file)

url = "https://bit.ly/3sIK2x5"

test_local = ocr_url(url=url, api_key=api_key)
dictionary = json.loads(test_local)
result = dictionary["ParsedResults"][0]["ParsedText"]
result
