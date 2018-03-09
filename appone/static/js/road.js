var vertexHeight = 15000;
var planeDefinition = 100;
var planeSize = 1245000;
var totalObjects = 50000;
var frame = 0;
var i, j,  particles = []; 
//画散点图
$(document).ready(function(){
$.getJSON('/prediction/', function (ret) {
    for (var j = 0; j < 140; j+=2) {		
        var dian_geometry = new THREE.SphereGeometry(500, 10, 10);
        if(ret.abnormalratio[j] / ret.abnormalratio[j+1]>0.9)  var dian_material = new THREE.MeshLambertMaterial({ color: 0xff3300 });
        else if(ret.abnormalratio[j] / ret.abnormalratio[j+1]>0.7) var dian_material = new THREE.MeshLambertMaterial({ color: 0xff0066 });
        else if(ret.abnormalratio[j] / ret.abnormalratio[j+1]>0.5) var dian_material = new THREE.MeshLambertMaterial({ color: 0xff6699 });
        else if(ret.abnormalratio[j] / ret.abnormalratio[j+1]>0.3) var dian_material = new THREE.MeshLambertMaterial({ color: 0xff99cc });
        else if(ret.abnormalratio[j] / ret.abnormalratio[j+1]>0.1) var dian_material = new THREE.MeshLambertMaterial({ color: 0xffccff });
        else var dian_material = new THREE.MeshLambertMaterial({ color: 0x33ff00 });
        var star = new THREE.Mesh(dian_geometry, dian_material);
        scene.add(star);
        star.position.x = 12000 + 2000 * (j/2)-20000*parseInt(j/20);
        if(ret.abnormalratio[j+1]==0)  star.position.y = 10000;
        else star.position.y = (ret.abnormalratio [j]/ ret.abnormalratio[j+1]) * 20000 + 10000;//console.log(ret.abnormalratio[j] / ret.abnormalratio[j+1]);
        star.position.z = 450000-50000*parseInt(j/20);
    }
    // var len_5VM45975 = 0;
    // for (var i = 140; i < 150; i++) {
    //     len_5VM45975 += parseInt(ret[i]);console.log(len_5VM45975);
    // };

    // for (var j = 140; j <150; j++) {
		
    //     var dian_geometry = new THREE.SphereGeometry(500, 10, 10);
    //     var dian_material = new THREE.MeshLambertMaterial({ color: 0xff3300 });
    //     var star = new THREE.Mesh(dian_geometry, dian_material);
    //     scene.add(star);
    //     star.position.x = -(10000 + 2000 * (j-140));
    //     star.position.y = (ret[j] / len_5VM45975) * 20000 + 10000;console.log(ret[j] / len_5VM45975);
    //     star.position.z = 450000;
    // }
    

    // var len_S2A58BGQ = 0;
    // for (var i = 10; i < 20; i++) {
    //     len_S2A58BGQ += parseInt(ret[i][0]);
    // };

    // for (var j = 10; j < 20; j++) {
		
    //     var dian_geometry = new THREE.SphereGeometry(500, 10, 10);
    //     var dian_material = new THREE.MeshLambertMaterial({ color: 0xff3300 });
    //     var star = new THREE.Mesh(dian_geometry, dian_material);
    //     scene.add(star);
    //     star.position.x = 10000 + 2000 * (j-10);
    //     star.position.y = (ret[j][0] / len_S2A58BGQ) * 20000 + 10000;//console.log(ret[j][0]/len_S2A58BGQ);
    //     //maybe sth worry here
    //     star.position.z = 400000;
    // }

    // var len_WDWCASZ0627345 = 0;
    // for (var i = 20; i < 30; i++) {
    //     len_WDWCASZ0627345 += parseInt(ret[i][0]);
    // };

    // for (var j = 20; j < 30; j++) {
		
    //     var dian_geometry = new THREE.SphereGeometry(500, 10, 10);
    //     var dian_material = new THREE.MeshLambertMaterial({ color: 0xff3300 });
    //     var star = new THREE.Mesh(dian_geometry, dian_material);
    //     scene.add(star);
    //     star.position.x = 10000 + 2000 * (j-20);
    //     star.position.y = (ret[j][0] / len_WDWCASZ0627345) * 20000 + 10000;//console.log(ret[j][0]/len_WDWCASZ0627345);
    //     //maybe sth worry here
    //     star.position.z = 350000;
    // }

    // var len_Z1D3XB0A = 0;
    // for (var i = 30; i < 40; i++) {
    //     len_Z1D3XB0A += parseInt(ret[i][0]);
    // };

    // for (var j = 30; j < 40; j++) {
		
    //     var dian_geometry = new THREE.SphereGeometry(500, 10, 10);
    //     var dian_material = new THREE.MeshLambertMaterial({ color: 0xff3300 });
    //     var star = new THREE.Mesh(dian_geometry, dian_material);
    //     scene.add(star);
    //     star.position.x = 10000 + 2000 * (j-30);
    //     star.position.y = (ret[j][0] / len_Z1D3XB0A) * 20000 + 10000;//console.log(ret[j][0]/len_Z1D3XB0A);
    //     //maybe sth worry here
    //     star.position.z = 300000;
    // }

    // var len_Z4YAZWRB = 0;
    // for (var i = 40; i < 50; i++) {
    //     len_Z4YAZWRB += parseInt(ret[i][0]);
    // };

    // for (var j = 40; j < 50; j++) {
		
    //     var dian_geometry = new THREE.SphereGeometry(500, 10, 10);
    //     var dian_material = new THREE.MeshLambertMaterial({ color: 0xff3300 });
    //     var star = new THREE.Mesh(dian_geometry, dian_material);
    //     scene.add(star);
    //     star.position.x = 10000 + 2000 * (j-40);
    //     star.position.y = (ret[j][0] / len_Z4YAZWRB) * 20000 + 10000;console.log(ret[j][0]/len_Z4YAZWRB);
    //     //maybe sth worry here
    //     star.position.z = 250000;
    // }
})
});

var container = document.createElement('div');
document.body.appendChild(container);

var camera = new THREE.PerspectiveCamera(55, window.innerWidth / window.innerHeight, 1, 400000)
camera.position.x = 0;
camera.position.z = 550000;
camera.position.y = 10000;
camera.lookAt(new THREE.Vector3(0, 6000, 0));


var scene = new THREE.Scene();
scene.fog = new THREE.Fog(0x23233f, 1, 300000);
var light = new THREE.DirectionalLight(0xffffff);
light.position.set(0, 10000, 550000);
scene.add(light);
var uniforms =
    {
        time: { type: "f", value: 0.0 }// uniforms通过这个属性可以向你的着色器发信息。同样的信息会发送到每一个顶点和片元
    };

var material = new THREE.ShaderMaterial({
    uniforms: uniforms,
    vertexShader: document.getElementById('vertexShader').textContent,//vertexShader(顶点着色器)/这个着色器允许你修改每一个传入的顶点的位置
    fragmentShader: document.getElementById('fragmentShader').textContent,//fragementShader(片元着色器)/这个着色器定义的是每个传入的像素颜色
    wireframe: true,
    fog: false
});

//定义长方型，后两个参数表示分段
var plane = new THREE.Mesh(new THREE.PlaneGeometry(planeSize, planeSize, planeDefinition, planeDefinition), material);
plane.rotation.x -= Math.PI * .5;

scene.add(plane);

var geometry = new THREE.Geometry();

for (i = 0; i < totalObjects; i++) {
    var vertex = new THREE.Vector3();//返回沿当前三维线段方向的任意向量
    vertex.x = Math.random() * planeSize - (planeSize * .5);
    vertex.y = (Math.random() * 100000) + 10000;
    vertex.z = Math.random() * planeSize - (planeSize * .5);
    geometry.vertices.push(vertex);
}
var material = new THREE.ParticleBasicMaterial({ size: 200 });
var particles = new THREE.ParticleSystem(geometry, material);
scene.add(particles);

//画网格 right2
//x1,x2为x轴方向起、止x坐标
//y1,y2为y轴方向起、止y坐标
//ystart,xstart画平行y,z轴线条时的起始y,x坐标
//z图形位于z平面层次
//interval每隔多远画一条线
//linenum画线的总数
function drawGridRight(x1, x2, y1, y2, ystart, xstart, z, interval, linenum) {
    var material_r2 = new THREE.LineBasicMaterial({ color: 0xffffff });
    var geometry_r2 = new THREE.Geometry();
    geometry_r2.vertices.push(new THREE.Vector3(x1, 0, z));
    geometry_r2.vertices.push(new THREE.Vector3(x2, 0, z));
    for (var i = 0; i <= linenum; i++) {
        var line_r2 = new THREE.Line(geometry_r2, material_r2);
        line_r2.position.y = (i * interval) + ystart;
        scene.add(line_r2);
    }
    var material_r2 = new THREE.LineBasicMaterial({ color: 0xffffff });
    var geometry_r2 = new THREE.Geometry();
    geometry_r2.vertices.push(new THREE.Vector3(0, y1, z));
    geometry_r2.vertices.push(new THREE.Vector3(0, y2, z));
    for (var i = 0; i <= linenum; i++) {
        var line_r2 = new THREE.Line(geometry_r2, material_r2);
        line_r2.position.x = (i * interval) + xstart;
        scene.add(line_r2);
    }
}
function drawGridLeft(x1, x2, y1, y2, ystart, xstart, z, interval, linenum) {
    var material_r2 = new THREE.LineBasicMaterial({ color: 0xffffff });
    var geometry_r2 = new THREE.Geometry();
    geometry_r2.vertices.push(new THREE.Vector3(x1, 0, z));
    geometry_r2.vertices.push(new THREE.Vector3(x2, 0, z));
    for (var i = 0; i <= linenum; i++) {
        var line_r2 = new THREE.Line(geometry_r2, material_r2);
        line_r2.position.y = (i * interval) + ystart;
        scene.add(line_r2);
    }
    var material_r2 = new THREE.LineBasicMaterial({ color: 0xffffff });
    var geometry_r2 = new THREE.Geometry();
    geometry_r2.vertices.push(new THREE.Vector3(0, y1, z));
    geometry_r2.vertices.push(new THREE.Vector3(0, y2, z));
    for (var i = 0; i <= linenum; i++) {
        var line_r2 = new THREE.Line(geometry_r2, material_r2);
        line_r2.position.x = -(i * interval) + xstart;
        scene.add(line_r2);
    }
}
drawGridRight(10000, 30000, 10000, 30000, 10000, 10000, 400000, 2000, 10);
drawGridRight(10000, 30000, 10000, 30000, 10000, 10000, 450000, 2000, 10);
drawGridLeft(-10000, -30000, 10000, 30000, 10000, -10000, 400000, 2000, 10);
drawGridLeft(-10000, -30000, 10000, 30000, 10000, -10000, 450000, 2000, 10);

drawGridRight(10000, 30000, 10000, 30000, 10000, 10000, 300000, 2000, 10);
drawGridRight(10000, 30000, 10000, 30000, 10000, 10000, 350000, 2000, 10);
drawGridLeft(-10000, -30000, 10000, 30000, 10000, -10000, 300000, 2000, 10);
drawGridLeft(-10000, -30000, 10000, 30000, 10000, -10000, 350000, 2000, 10);
drawGridRight(10000, 30000, 10000, 30000, 10000, 10000, 200000, 2000, 10);
drawGridRight(10000, 30000, 10000, 30000, 10000, 10000, 250000, 2000, 10);
drawGridLeft(-10000, -30000, 10000, 30000, 10000, -10000, 200000, 2000, 10);
drawGridLeft(-10000, -30000, 10000, 30000, 10000, -10000, 250000, 2000, 10);
drawGridRight(10000, 30000, 10000, 30000, 10000, 10000, 100000, 2000, 10);
drawGridRight(10000, 30000, 10000, 30000, 10000, 10000, 150000, 2000, 10);
drawGridLeft(-10000, -30000, 10000, 30000, 10000, -10000, 100000, 2000, 10);
drawGridLeft(-10000, -30000, 10000, 30000, 10000, -10000, 150000, 2000, 10);
drawGridRight(10000, 30000, 10000, 30000, 10000, 10000, 0, 2000, 10);
drawGridRight(10000, 30000, 10000, 30000, 10000, 10000, 50000, 2000, 10);
drawGridLeft(-10000, -30000, 10000, 30000, 10000, -10000, 0, 2000, 10);
drawGridLeft(-10000, -30000, 10000, 30000, 10000, -10000, 50000, 2000, 10);

//添加标题
function titleRight(username,z) {
    var material = new THREE.MeshPhongMaterial({
        color: 0x66ccff,
        specular: 0x66ccff,
        shininess: 0
    });
    var loader = new THREE.FontLoader();
    loader.load('../static/fonts/helvetiker_regular.typeface.json', function (font) {
        var mesh = new THREE.Mesh(new THREE.TextGeometry(username, {
            font: font,
            size: 1000,
            height: 1000
        }), material);
        mesh.position.set(16000,32000, z);
        scene.add(mesh);
    });
}
function titleLeft(username,z) {
    var material = new THREE.MeshPhongMaterial({
        color: 0x66ccff,
        specular: 0x66ccff,
        shininess: 0
    });
    var loader = new THREE.FontLoader();
    loader.load('../static/fonts/helvetiker_regular.typeface.json', function (font) {
        var mesh = new THREE.Mesh(new THREE.TextGeometry(username, {
            font: font,
            size: 1000,
            height: 1000
        }), material);
        mesh.position.set(-24000,32000, z);
        scene.add(mesh);
    });
}
titleRight('5VM45975',450000);
titleRight('S2A58BGQ',400000);
titleRight('WDWCASZ0627345',350000);
titleRight('Z1D3XB0A',300000);
titleRight('Z4YAZWRB',250000);
titleRight('537TT03OT',200000);
titleRight('Z4YAZTH6',150000);

titleLeft('5VM45975',450000);
titleLeft('S2A58BGQ',400000);
titleLeft('WDWCASZ0627345',350000);
titleLeft('Z1D3XB0A',300000);
titleLeft('Z4YAZWRB',250000);
titleLeft('537TT03OT',200000);
titleLeft('Z4YAZTH6',150000);

//添加坐标变量
function axisflagRight(x1, y1, x2, y2, z) {
    var material = new THREE.MeshPhongMaterial({
        color: 0x66ccff,
        specular: 0x66ccff,
        shininess: 0
    });
    var loader = new THREE.FontLoader();
    loader.load('../static/fonts/helvetiker_regular.typeface.json', function (font) {
        var mesh = new THREE.Mesh(new THREE.TextGeometry('date', {
            font: font,
            size: 800,
            height: 800
        }), material);
        mesh.position.set(x1, y1, z);
        scene.add(mesh);
        var mesh = new THREE.Mesh(new THREE.TextGeometry('abnormal_ratio', {
            font: font,
            size: 800,
            height: 800
        }), material);
        mesh.position.set(x2, y2, z);
        scene.add(mesh);
    });
}
function axisflagLeft(x1, y1, x2, y2, z) {
    var material = new THREE.MeshPhongMaterial({
        color: 0x66ccff,
        specular: 0x66ccff,
        shininess: 0
    });
    var loader = new THREE.FontLoader();
    loader.load('../static/fonts/helvetiker_regular.typeface.json', function (font) {
        var mesh = new THREE.Mesh(new THREE.TextGeometry('lstm', {
            font: font,
            size: 800,
            height: 800
        }), material);
        mesh.position.set(x1, y1, z);
        scene.add(mesh);
        var mesh = new THREE.Mesh(new THREE.TextGeometry('lstm_ratio', {
            font: font,
            size: 800,
            height: 800
        }), material);
        mesh.position.set(x2, y2, z);
        scene.add(mesh);
    });
}
axisflagRight(32000, 8000, 2000, 32000, 450000);
axisflagRight(32000, 8000, 2000, 32000, 400000);
axisflagLeft(-32000, 8000, -9000, 32000, 450000);
axisflagLeft(-32000, 8000, -9000, 32000, 400000);

axisflagRight(32000, 8000, 2000, 32000, 350000);
axisflagRight(32000, 8000, 2000, 32000, 300000);
axisflagLeft(-32000, 8000, -9000, 32000, 350000);
axisflagLeft(-32000, 8000, -9000, 32000, 300000);
axisflagRight(32000, 8000, 2000, 32000, 250000);
axisflagRight(32000, 8000, 2000, 32000, 200000);
axisflagLeft(-32000, 8000, -9000, 32000, 250000);
axisflagLeft(-32000, 8000, -9000, 32000, 200000);
axisflagRight(32000, 8000, 2000, 32000, 250000);
axisflagRight(32000, 8000, 2000, 32000, 200000);
axisflagLeft(-32000, 8000, -9000, 32000, 250000);
axisflagLeft(-32000, 8000, -9000, 32000, 200000);
axisflagRight(32000, 8000, 2000, 32000, 150000);
axisflagRight(32000, 8000, 2000, 32000, 100000);
axisflagLeft(-32000, 8000, -9000, 32000, 150000);
axisflagLeft(-32000, 8000, -9000, 32000, 100000);
axisflagRight(32000, 8000, 2000, 32000, 50000);
axisflagRight(32000, 8000, 2000, 32000, 0);
axisflagLeft(-32000, 8000, -9000, 32000, 50000);
axisflagLeft(-32000, 8000, -9000, 32000, 0);

//添加坐标刻度
//ystart,xstart画平行y,z轴的刻度时的起始y,x坐标
//interval每隔多远画一个刻度
//a y轴刻度的x坐标,b x轴刻度的y坐标,c层次
function axisvalueRight(xstart, ystart, interval, a, b, c) {
    var materialtext = new THREE.MeshPhongMaterial({
        color: 0xffffff,
        specular: 0xffffff,
        shininess: 0
    });
    var loader = new THREE.FontLoader();
    //right 1
    loader.load('../static/fonts/helvetiker_regular.typeface.json', function (font) {
        for (i = 0; i <= 10; i++) {
            var x = xstart + interval * i;
            var value = i ;
            var meshtextx = new THREE.Mesh(new THREE.TextGeometry(value, {
                font: font,
                size: 800,
                height: 0.1
            }), materialtext);
            meshtextx.position.set(x, b, c);
            scene.add(meshtextx);
        }
    });
    loader.load('../static/fonts/helvetiker_regular.typeface.json', function (font) {
        for (i = 0; i <= 10; i++) {
            var y = ystart + interval * i;
            var value = i / 10;
            var meshtextx = new THREE.Mesh(new THREE.TextGeometry(value, {
                font: font,
                size: 800,
                height: 0.1
            }), materialtext);
            meshtextx.position.set(a, y, c);
            scene.add(meshtextx);
        }
    });
}
function axisvalueLeft(xstart, ystart, interval, a, b, c) {
    var materialtext = new THREE.MeshPhongMaterial({
        color: 0xffffff,
        specular: 0xffffff,
        shininess: 0
    });
    var loader = new THREE.FontLoader();
    //right 1
    loader.load('../static/fonts/helvetiker_regular.typeface.json', function (font) {
        for (i = 0; i < 10; i++) {
            var x = -xstart - interval * i;
            var value = i/10 ;
            var meshtextx = new THREE.Mesh(new THREE.TextGeometry(value, {
                font: font,
                size: 800,
                height: 0.1
            }), materialtext);
            meshtextx.position.set(x, b, c);
            scene.add(meshtextx);
        }
    });
    loader.load('../static/fonts/helvetiker_regular.typeface.json', function (font) {
        for (i = 0; i < 10; i++) {
            var y = ystart + interval * i;
            var value = i / 10;
            var meshtextx = new THREE.Mesh(new THREE.TextGeometry(value, {
                font: font,
                size: 800,
                height: 0.1
            }), materialtext);
            meshtextx.position.set(a, y, c);
            scene.add(meshtextx);
        }
    });
}
axisvalueRight(10000, 10000, 2000, 8000, 8000, 400000);
axisvalueRight(10000, 10000, 2000, 8000, 8000, 450000);
axisvalueLeft(10000, 10000, 2000, -8000, 8000, 400000);
axisvalueLeft(10000, 10000, 2000, -8000, 8000, 450000);

axisvalueRight(10000, 10000, 2000, 8000, 8000, 300000);
axisvalueRight(10000, 10000, 2000, 8000, 8000, 350000);
axisvalueLeft(10000, 10000, 2000, -8000, 8000, 300000);
axisvalueLeft(10000, 10000, 2000, -8000, 8000, 350000);
axisvalueRight(10000, 10000, 2000, 8000, 8000, 200000);
axisvalueRight(10000, 10000, 2000, 8000, 8000, 250000);
axisvalueLeft(10000, 10000, 2000, -8000, 8000, 200000);
axisvalueLeft(10000, 10000, 2000, -8000, 8000, 250000);
axisvalueRight(10000, 10000, 2000, 8000, 8000, 100000);
axisvalueRight(10000, 10000, 2000, 8000, 8000, 150000);
axisvalueLeft(10000, 10000, 2000, -8000, 8000, 100000);
axisvalueLeft(10000, 10000, 2000, -8000, 8000, 150000);
axisvalueRight(10000, 10000, 2000, 8000, 8000, 50000);
axisvalueRight(10000, 10000, 2000, 8000, 8000, 0);
axisvalueLeft(10000, 10000, 2000, -8000, 8000, 50000);
axisvalueLeft(10000, 10000, 2000, -8000, 8000, 0);

//画坐标方向
function arrow(x1, y1, x2, y2, x3, y3, z, length) {
    var originx = new THREE.Vector3(x1, y1, z);//箭头始点坐标
    var terminusx = new THREE.Vector3(x2, y2, z);//箭头终点坐标
    var directionx = new THREE.Vector3().subVectors(terminusx, originx).normalize();//箭头方向
    var arrowx = new THREE.ArrowHelper(directionx, originx, length, 0xffffff);//箭头长度2500是指整个箭头长度
    scene.add(arrowx);//将箭头加入场景
    var originy = new THREE.Vector3(x1, y1, z);
    var terminusy = new THREE.Vector3(x3, y3, z);
    var directiony = new THREE.Vector3().subVectors(terminusy, originy).normalize();
    var arrowy = new THREE.ArrowHelper(directiony, originy, length, 0xffffff);
    scene.add(arrowy);
}
arrow(10000, 10000, 30000, 10000, 10000, 30000, 450000, 25000);
arrow(10000, 10000, 30000, 10000, 10000, 30000, 400000, 25000);
arrow(-10000, 10000, -30000, 10000, -10000, 30000, 450000, 25000);
arrow(-10000, 10000, -30000, 10000, -10000, 30000, 400000, 25000);

arrow(10000, 10000, 30000, 10000, 10000, 30000, 350000, 25000);
arrow(10000, 10000, 30000, 10000, 10000, 30000, 300000, 25000);
arrow(-10000, 10000, -30000, 10000, -10000, 30000, 350000, 25000);
arrow(-10000, 10000, -30000, 10000, -10000, 30000, 300000, 25000);
arrow(10000, 10000, 30000, 10000, 10000, 30000, 250000, 25000);
arrow(10000, 10000, 30000, 10000, 10000, 30000, 200000, 25000);
arrow(-10000, 10000, -30000, 10000, -10000, 30000, 250000, 25000);
arrow(-10000, 10000, -30000, 10000, -10000, 30000, 200000, 25000);
arrow(10000, 10000, 30000, 10000, 10000, 30000, 150000, 25000);
arrow(10000, 10000, 30000, 10000, 10000, 30000, 100000, 25000);
arrow(-10000, 10000, -30000, 10000, -10000, 30000, 150000, 25000);
arrow(-10000, 10000, -30000, 10000, -10000, 30000, 100000, 25000);
arrow(10000, 10000, 30000, 10000, 10000, 30000, 50000, 25000);
arrow(10000, 10000, 30000, 10000, 10000, 30000, 0, 25000);
arrow(-10000, 10000, -30000, 10000, -10000, 30000, 50000, 25000);
arrow(-10000, 10000, -30000, 10000, -10000, 30000, 0, 25000);

var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
container.appendChild(renderer.domElement);

render();

function render() {
    requestAnimationFrame(render);
    if (camera.position.z <= 0)
        camera.position.z = 550000;
    else
        camera.position.z -= 200;
    uniforms.time.value = frame;
    frame += .04;
    //  dateVerts();
    renderer.render(scene, camera);
}