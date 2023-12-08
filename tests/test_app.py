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
    page.goto(f"http://{test_web_address}/albums/all_albums")
    h1_tag = page.locator("h1")
    p_tag = page.locator("p")
    expect(h1_tag).to_have_text(["Doolittle", "Surfer Rosa", "Waterloo", "Super Trouper"])
    expect(p_tag).to_have_text([
        "Release year: 1989\nArtist: Pixies",
        "Release year: 1988\nArtist: Pixies",
        "Release year: 1974\nArtist: ABBA",
        "Release year: 1980\nArtist: ABBA"
        ])
    page.click('a')
    expect(h1_tag).to_have_text("Doolittle")
    

def test_get_single_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/single_album/1")
    h1_tag = page.locator("h1")
    p_tag = page.locator("p")
    expect(h1_tag).to_have_text("Doolittle")
    expect(p_tag).to_have_text("Release year: 1989\nArtist: Pixies")

    page.goto(f"http://{test_web_address}/albums/single_album/2")
    h1_tag = page.locator("h1")
    p_tag = page.locator("p")
    expect(h1_tag).to_have_text("Surfer Rosa")
    expect(p_tag).to_have_text("Release year: 1988\nArtist: Pixies")


def test_visit_album_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/single_album/1")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Doolittle")
    