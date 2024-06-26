const puppeteer = require("puppeteer");

(async () => {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();

  const URL = "https://scifigurmeet.github.io/magicwebsite/";
  console.log(URL);

  try {
    await page.goto(URL);

    await page.waitForSelector('h1:contains("Gurmeet")', { timeout: 10000 });

    console.log("Test Passed: Found h1 tag containing 'Gurmeet'");
  } catch (error) {
    console.error("Test Failed:", error);
  } finally {
    await browser.close();
  }
})();