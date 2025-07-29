import requests

def get_definition(word):
    """
    Yeh function dictionaryapi.dev se word ki definition, pronunciation,
    part of speech, aur example sentences fetch karta hai.
    """
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code != 200:
            return {
                "error": f"⚠️ Failed to fetch definition (status {response.status_code})"
            }
        data = response.json()
        if not data or not isinstance(data, list):
            return {"error": "❌ No definition found."}
        
        # Pehla entry lete hain
        entry = data[0]
        word_info = {
            "word": entry.get("word", ""),
            "phonetics": [],
            "meanings": []
        }
        
        # Pronunciation nikalte hain
        phonetics = entry.get("phonetics", [])
        for phon in phonetics:
            text = phon.get("text")
            audio = phon.get("audio")
            if text or audio:
                word_info["phonetics"].append({"text": text, "audio": audio})
        
        # Meanings nikalte hain
        meanings = entry.get("meanings", [])
        for meaning in meanings:
            part_of_speech = meaning.get("partOfSpeech", "")
            definitions = meaning.get("definitions", [])
            defs = []
            for d in definitions:
                definition = d.get("definition", "")
                example = d.get("example", "")
                defs.append({"definition": definition, "example": example})
            word_info["meanings"].append({
                "partOfSpeech": part_of_speech,
                "definitions": defs
            })
        
        return word_info
    except Exception as e:
        return {"error": f"❌ Error: {str(e)}"}
