# What is?
サンデー写真家向けの画像整理スクリプトです。  
このスクリプトを実行することで、不要なRaw画像を一括で削除することができます。  
Windows10環境のみで動作を確認しています。  
  
# Usage
仕分けしたい画像ファイルと同じ階層にスクリプトをコピーしてください。  
削除したい写真のjpgファイルのみを削除し、全て削除し終えたらこのスクリプトを実行します。  
スクリプト実行後、削除しなかったjpgファイルと同名のrawファイルのみが残ります。  
  
# Example
<階層構成>  
　dir/  
　├ This script  
　├ hoge1.jpg  
　├ hoge1.raw  
　├ hoge2.jpg  
　├ hoge2.raw  
　├ hoge3.jpg  
　├ hoge3.raw 
　├ hoge4.jpg  
　└ hoge4.raw  
   
上の階層の例で、hoge1.jpg, hoge3.jpgを削除します。  
  
　dir/  
　├ This script  
　├ hoge1.raw  
　├ hoge2.jpg  
　├ hoge2.raw  
　├ hoge3.raw 
　├ hoge4.jpg  
　└ hoge4.raw  
   
この状態で本スクリプトを実行することで、次のようになります。  
  
　dir/  
　├ This script  
　├ hoge2.jpg  
　├ hoge2.raw  
　├ hoge4.jpg  
　└ hoge4.raw  
 
# Development environment
Python 3.6  
Windows10 pro x64 1903  
