from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===


def test_get_albums(page, test_web_address, db_connection): # Note new parameters
    db_connection.seed("seeds/music_library.sql")
    
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/albums")
    # We look at the <div> tag
    div_tag = page.locator("div")
    expect(div_tag).to_have_text(["Title: Doolittle\nReleased: 1989", "Title: Surfer Rosa\nReleased: 1988", "Title: Waterloo\nReleased: 1974", "Title: Super Trouper\nReleased: 1980"])
