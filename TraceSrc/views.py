from django.shortcuts import render
from TraceSrc.Algorithm import findPath
from TraceSrc.Algorithm import py2js
from django.views.decorators.csrf import csrf_exempt
from TraceSrc.Algorithm.data import allVertices

ctx = dict()
# index front-to-end connector
@csrf_exempt
def index(req):
    # 在这里调整追踪0还是溯源1
    # 前端只需要在这里处理即可
    direct = {'forwards':0, 'backwards':1}
    '''pyPath = findPath.process('V%d' % startNum, direct[directNum])
    jsPath = py2js.parse(pyPath)
    print(jsPath)
    print(type(jsPath))
    f.write(jsPath)
    f.close()'''
    
    if req.is_ajax():
        #print(req.POST)
        ctx['current_start'] = ""
        ctx['current_direct'] = '显示全图'
        f = open(r'templates/scripts/args.txt', 'w')
        startNum = int(req.POST['point'])
        directNum = req.POST['direct']
        pyPath = findPath.process('V%d' % startNum, direct[directNum])
        jsPath = py2js.parse(pyPath)
        f.write(jsPath)
        f.close()  
        if startNum != 0:
            for v in allVertices:
                if v['id'] == startNum:
                    ctx['current_start'] = v['label']
                    break
            if directNum == "forwards":
                ctx['current_direct'] = '向下追踪'
            else:
                ctx['current_direct'] = '向上溯源'
    f = open(r'templates/scripts/args.txt', 'r')
    ctx['graph'] = f.read()
    f.close()
    return render(req, r'../templates/pages/graph.html', ctx)
