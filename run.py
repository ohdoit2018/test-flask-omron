from flask import Flask, render_template

from modules import BasicProcess

app = Flask(__name__)
bp = BasicProcess()

'''
@app.route("/")
def hello_world():
    message = "Hello Python!"
    return render_template("test.html", message = message)
'''

#@app.route("/front_test")
@app.route("/")
def front_test():
    dbData = bp.getDBCalorie()
    if not dbData: # DBが空だったら
        calorieperdayForGraph = {}
        calorieperfiftForGraph = {}
    else:
        calories = bp.shapeCalorieData(dbData)
        calorieperday, currentDay = bp.getDayConsumedCalorie(calories)
        calorieperfift = bp.get15minConsumedCaloire(calories)

        calorieperdayForGraph = bp.getGraphDatas(calorieperday, 15) # キロに変換するのはJS側で．
        calorieperfiftForGraph = bp.getGraphDatas(calorieperfift, 15)
        currentCalorie = round(calorieperdayForGraph[currentDay]/1000,2) # ここで小数点以下2桁に整形
        restCalorie = round(bp.getRestCalorie(calorieperday),2) # ここで小数点以下2桁に整形
        exerciseRank, movieNum = bp.selectExercise(calorieperfiftForGraph)
        if exerciseRank=="達成済":
            restCalorie = 0

        # 確認用
        #print("\n\n\n\n(dbData): {0}\n\n\n\n".format(dbData))
        #print("\n\n\n\n(calorieperfiftForGraph): {0}\n\n\n\n".format(calorieperfiftForGraph))
        
    return render_template("front_test.html", 
                calorieperday = calorieperdayForGraph, # リストに日本語含めないように．含める場合はテンプレート側のtojsonでは対応しにくい．
                calorieperfift = calorieperfiftForGraph,
                currentCalorie = currentCalorie,
                restCalorie = restCalorie,
                exerciseRank = exerciseRank,
                movieNum = movieNum
                )

@app.route("/test_postgresql")
def hello_postgresql():
    dbData = bp.getDBCalorie()
    calories = bp.shapeCalorieData(dbData)
    calorieperday, currentDay = bp.getDayConsumedCalorie(calories)
    return render_template("test.html", psqldatas = calories, calorieperday = calorieperday)

if __name__ == "__main__":
    app.run()