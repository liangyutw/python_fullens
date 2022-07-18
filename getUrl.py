import demo
import define
import functions as func
from datetime import datetime

# 開始計時
start_ = datetime.utcnow()

# 分隔線開始
demo.divider()



allUrl = func.singleUrl(define.mainUrl)

# 檢查404網址
get404Result = func.get404List(allUrl)

if len(get404Result) > 0:
    print(len(get404Result))
else:
    result = func.mainLogic(allUrl)
    if result != True:
        print('存檔失敗')
    else:
        print('存檔完成')

# 分隔線結束
demo.divider()

# 結束計時
end_ = datetime.utcnow()
c = (end_ - start_)
print(c)
