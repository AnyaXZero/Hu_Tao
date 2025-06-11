from AnieXEricaMusic.utils.mongo import db

coupledb = db.couple

async def _get_lovers(cid: int):
    lovers = await coupledb.find_one({"chat_id": cid})
    if lovers and "couple" in lovers:
        return lovers["couple"]
    else:
        return {}

async def _get_image(cid: int):
    lovers = await coupledb.find_one({"chat_id": cid})
    if lovers and "img" in lovers:
        return lovers["img"]
    else:
        return {}

async def get_couple(cid: int, date: str):
    lovers = await _get_lovers(cid)
    if date in lovers:
        return lovers[date]
    else:
        return False

async def save_couple(cid: int, date: str, couple: dict, img: str):
    lovers = await _get_lovers(cid)
    
    # Ensure 'couple' is a dictionary and 'img' is a string (URL or image path)
    if not isinstance(couple, dict):
        raise ValueError("Couple data should be a dictionary")
    if not isinstance(img, str):
        raise ValueError("Image URL should be a string")
    
    lovers[date] = couple
    await coupledb.update_one(
        {"chat_id": cid},
        {"$set": {"couple": lovers, "img": {date: img}}},
        upsert=True,
    )
