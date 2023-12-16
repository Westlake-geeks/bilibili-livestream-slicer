# bilibili-livestream-slicer （自动切片机）

如果您要成功运行这个代码，您需要高超的环境管理能力。包括但不限于熟练掌握 `pip install` 、 'baidu search' 、'google search'。

你需要准备以下内容：
1. 相关的 `python` 库，其中 `openai-python==0.28` （更高版本会失效，其他库装最新的应该就可以）。
2. 命令行可以实现 `ffmpeg` 的运行，可以直接使用 `conda install ffmpeg` 来安装。（加在环境变量里面）
3. 稳定的翻越 *THE GREAT FIREWALL* 的能力，以下载 `whisper` 的  `midium` 模型的参数。（越 1.4G）
4. 命令行可以实现 `chromedriver` 的运行，请下载对应电脑上的谷歌浏览器版本的 `chromedriver`。（加在环境变量里面）

如果你希望这个代码得到应有的效果，你*可能*需要修改以下内容：
1. 代码里的绝对路径。
2. `cookie.txt` 里面的内容。
3. `Openai` 的 api。
4. `Credential` 内的内容。

# bilibili-livestream-slicer 

To successfully run this code, you will need advanced environment management skills, including but not limited to proficiency in `pip install`, 'baidu search', and 'google search'.

You will need to prepare the following:
1. Relevant Python libraries, with `openai-python==0.28` (higher versions may not work; other libraries should be up-to-date).
2. The ability to run `ffmpeg` through the command line, which can be installed using `conda install ffmpeg` (add it to your environment variables).
3. A stable capability to bypass *THE GREAT FIREWALL* to download the parameters for the `midium` model of `whisper` (approximately 1.4G).
4. The ability to run `chromedriver` through the command line. Download the corresponding `chromedriver` version for your computer's Google Chrome browser (add it to your environment variables).

If you want this code to function as intended, you *may* need to modify the following:
1. Absolute paths within the code.
2. Contents of the `cookie.txt` file.
3. The `Openai` API.
4. Contents within the `Credential`.
