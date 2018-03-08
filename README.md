<h1>python_tools</h1>
<p>These are some small tools which can make some operations EZ!</p>

<h2>tab.py</h2>
<p>This is designed for add/delete specific Tabs.</p>
<p>This may be useful for Python IDEL.</p>

<h2>rename_to_folder.py</h2>
<p>This is designed for rename certain file into the name of the folder.</p>
<p>The working firectory is where you put <b>rename_to_folder.py</b>.</p>
<p>So, you can put <b>rename_to_folder.py</b> into the directory you want to make the change.</p>
<i>Notice: the function is not fully packaged, thus you should alter the code according to your needs.</i>

<h2>move_with_folder_created.py</h2>
<p>This is designed for copying folders containing specific files into a newly created directory.</p>
<p>The working is the where you put <b>move_with_folder_created.py</b> in and meanwhile is where the files are.</p>
<p>The target directory can be specified through input.</p>
<i>Notice: the function is not fully packaged, thus you should alter the code according to your needs.</i>

<h2>request_frame.py</h2>
<p>This is a basic frame for web scraping.</p>
<p><b>requests</b> is used in <b>request_frame.py</b>.</p>

<h2>ip_check.py</h2>
<p>You can use this script to check the address of IP. Also, you can check the address and IP of URL.</p>
<p><b>requests</b> is used in <b>ip_check.py</b>.</p>
<p>I use <a href = "http://ip.chinaz.com/"><b>http://ip.chinaz.com/</b></a> as the website to collect the information.</p>

<h2>csgo_inspect.py</h2>
<p><b>csgo_inspect.py</b> helps you to save the inspect picture of item you wanna inspect.</p>
<p>You only need to give the inspect link of the item and the path where you want to save the image.</p>
<p>I use <a href = 'https://metjm.net/csgo/'><b>https://metjm.net/csgo/</b></a> as the website to help me to realize the function.</p>
<p>Further more, I am developing script that can save all the inspect images given someone's the steam_id.</p>

<h2>json_reform.py</h2>
<p><b>json_reform.py</b> reads the json context from the file and output the reformed format.</p>
<p>It is designed for human preview.</p>
<p>Two functions can both realize the function.</p>
<p>You can easily redirect the output to your screen or files or whatever.<i>(**file template has been added)</i></p>

<h2>steam_id_checker.py</h2>
<p><b>steam_id_checker.py</b> is designed for checking the steam id given the customed steam id.</p>
<p>This script extracts information from <a href = 'steamid.xyz'><b>steamid.xyz</b></a>.</p>

<h2>csmoney.py</h2>
<p><b>csmoney.py</b> extracts the database of all the items currently on sell on <a href = 'https://cs.money'>https://cs.money</a>.</p>
<p>The output is <i>csmoney.json</i> with is a dictionary sorted by the item name.</p>
<p>The item name is regularized into 'name (QUALITY)'</p>
<p><b>It is only used for personal use (like local price checker) and no commercial use of it is allowed!</b></p>

<h2>skinhub.py</h2>
<p><b>skinhub.py</b> extracts the database of all the items currently on sell on <a href = 'https://skinhub.com/official'>https://skinhub.com/official</a>.</p>
<p>The output is <i>skinhub.json</i> with is a dictionary sorted by the item name.</p>
<p><b>It is only used for personal use (like local price checker) and no commercial use of it is allowed!</b></p>

<h2>price_compare.py</h2>
<p><b>price_compare.py</b> is designed for output the price gap collected from <a href = 'https://cs.money'>https://cs.money</a> and <a href = 'https://skinhub.com/official'>https://skinhub.com/official</a>.</p>
<p>The output is ranked with the price ratio(csmoney/skinhub) DESC.</p>
<p>You can either run with the existing data in json form, or embed <b>csmoney.py</b> and <b>skinhub.py</b> into this script to get instant data statistics.</p>