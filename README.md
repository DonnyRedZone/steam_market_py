<h1>Steam-Market-Py</h1>

___

<h2>Features</h2>
<h3> Working </h3>
1. Steam Market Data
    1. Search The Market Hash Name of Any Item
    2. Current Price of any item
    3. Full price History of Any item
    4. Number of listings for any item 
    5. Median Price for any Item

<h3> Planned </h3>

2. Steam Player Inventories 
    1. Read What's in players' inventories
    2. Price each item in the inventory
    3. Price the full inventory (before and after tax)

3. Misc Things
    1. Get the thumbnail of any item

___

<h2> Getting Started </h2>

<h3> Installation </h3>

>pip install steam_market_py

or

`git.clone https://github.com/DonnyRedZone/steam_market_py` <br>
`cd steam_market_py` <br>
`python setup.py install`

>Imports as SteamMarket

<h3> Important! </h3>

**Many Features of this module rely on api calls that require you to enter browser cookies for steam** <br>
<h4> How do I get cookies!? </H4>
1. Go to store.steampowered.com
2. Sign in , If you sign out later in the future , you have to repeat this process
3. Click the little padlock in the address bar <br>![Padlock](https://i.imgur.com/IbOmkIP.png) <br>
4. click cookies ! <br>
![Cookies](https://i.imgur.com/ffnk9kJ.png)
   
5. Extend store.steampowered.com and extend cookies <br>
![extended](https://i.imgur.com/Wo4q9lV.png)
   
6. Scroll Down until you find 'steamLoginSecure' , click on it and copy everything from 'content' <br>
![laststep](https://i.imgur.com/xBUieEw.png)
   
Now you have your cookie ! Yay

7. Now you have a 2 options :
    1. Set the cookie using cmd (reccomended because you wont ever have to do it your code , out of sight , code and mind , make sure python is in your path!<br>
       `python` <br>
       `import SteamMarket` <br>
       `SteamMarket.set_cookies("your cookie")` <br>
       Make sure to put the cookie in quotes!
       
    2. Set the cookie in your code (does the same as above but its ugly to look at and will always be there) <br>
        `import SteamMarket` <br>
        `SteamMarket.set_cookies("your cookie")` <br>
       
>note : Steam Family View Breaks Everything , please turn it off 
       
Now cookies are done .. Yay!

___
<h2> Documentation </h2>

<h3> General Parameters </h3>

`appid` - Is the ID of the game you are looking items up for - [Search For Game's IDs](https://steamdb.info/search/?a=app&q=CS%3AGO&type=1&category=0)
<br> `hash_name` - Market Hash Name of The Item you are looking up found by using `SteamMarket.get_hash_name("search term")`

___
<h3> Find those annoying Market Hash names</h3>

`SteamMarket.get_hash_name("query")`
<br> searches what you enter as your query and returns the proper market hash name usable in the rest of the code
<br> it picks whatever is most relevant to your search , so it's helpful to be a bit more specific
<br>Example:
<br>`SteamMarket.get_hash_name(730,"Ak Redline Minimal Wear")`
<br> returns :
<br> `AK-47 | Redline (Field-Tested)`

___

<h3> Looking up current price of item </h3>

<h4>`SteamMarket.get_current_price (appid , hash_name , mode*, currency*) ` *-optional 
<br> Gets the current price of the item </h4>
<br> `currency` default - USD 
<br> numeric value corresponding to the currency you would like to make the call for
<br> you probabally want to add this dict somewhere in your code
<br> `curAbbrev = {
    'USD' : 1,
    'GBP' : 2,
    'EUR' : 3,
    'CHF' : 4,
    'RUB' : 5,
    'KRW' : 16,
    'CAD' : 20,
}
`
<br>
<br>
<br>`mode` - 1 or 2 or 3 (default is 1)
<br><br> 1. Uses Steam's Standard Api , Very Fast , Updates are slow ,Returns the lowest sell order , Api calls limited to 20 in 1 minute (put a 3 second wait between calls)
<br><br> 2. Uses Web Scraping to get current price , Slower in comparison , Updates as soon as there is a change in the lowest sell order , Returns the lowest sell order , No Call limit , DOES NOT NEED COOKIES ! , CANNOT CHANGE CURRENCY ALWAYS YOUR HOME CURRENCY
<br><br> 3. Uses Steam's Standard **History** Api , Very Fast , Updates as soon as there is a sale , Returns the price the last item actually sold for , No call limit , cannot change currency , stays as USD (Im planning on adding the option to change this to your home one by using cookies) 
<br><br> Example:
<br> `SteamMarket.get_current_price(730 , 'AK-47 | Redline (Field-Tested)' , 1 , 3)`
<br> Will return:
<br> Somewhere around `16,21€`

___

<h3> Getting Item Price History </h3>

`SteamMarket.get_price_history(appid,hash_name)` <br>


       
       
       









