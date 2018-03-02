var vertexHeight = 15000;
var planeDefinition = 100;
var planeSize = 1245000;
var totalObjects = 50000;
var frame = 0;
var i, j, datax = [10000, 10100, 10200, 10300, 10400, 10500, 10600, 10700, 10800, 10900], datay = [], particles = [], point;
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
light.density = 5000000;
light.shadow.camera.far = 4000000;
scene.add(light);
var light2 = new THREE.DirectionalLight(0xffffff);
light2.position.set(0, 10000, 300000);
light2.density = 5000000;
scene.add(light2);
var uniforms =
    {
        time: { type: "f", value: 0.0 }// uniforms通过这个属性可以向你的着色器发信息。同样的信息会发送到每一个顶点和片元
    };


//自己定制着色器ShaderMaterial
var material = new THREE.ShaderMaterial({
    uniforms: uniforms,
    vertexShader: document.getElementById('vertexShader').textContent,//vertexShader(顶点着色器)/这个着色器允许你修改每一个传入的顶点的位置
    fragmentShader: document.getElementById('fragmentShader').textContent,//fragementShader(片元着色器)/这个着色器定义的是每个传入的像素颜色
    wireframe: true,
    fog: false
});

var geometry = new THREE.Geometry();

for (i = 0; i < totalObjects / 2; i++) {
    var vertex = new THREE.Vector3();//返回沿当前三维线段方向的任意向量
    vertex.x = Math.random() * planeSize - (planeSize * .5);
    // vertex.y = (Math.random()*100000)+10000;
    vertex.z = Math.random() * planeSize - (planeSize * .5);
    geometry.vertices.push(vertex);
}
var material = new THREE.ParticleBasicMaterial({ size: 200 });
var particles = new THREE.ParticleSystem(geometry, material);
scene.add(particles);
//画球体
for (i = 0; i < 100; i++) {
    var dian_geometry = new THREE.SphereGeometry(1000, 10, 10);
    var dian_material = new THREE.MeshLambertMaterial({ color: 0xffff00 });
    var star = new THREE.Mesh(dian_geometry, dian_material);
    scene.add(star);
    star.position.x = Math.random() * planeSize - (planeSize * .5);
    star.position.y = Math.random() * 40000 + 40000;
    star.position.z = Math.random() * planeSize - (planeSize * .5);
}
for (i = 0; i < 100; i++) {
    var dian_geometry = new THREE.SphereGeometry(1000, 10, 10);
    var dian_material = new THREE.MeshLambertMaterial({ color: 0xff0033 });
    var star = new THREE.Mesh(dian_geometry, dian_material);
    scene.add(star);
    star.position.x = Math.random() * planeSize - (planeSize * .5);
    star.position.y = Math.random() * 40000 + 40000;
    star.position.z = Math.random() * planeSize - (planeSize * .5);
}
for (i = 0; i < 100; i++) {
    var dian_geometry = new THREE.SphereGeometry(1000, 10, 10);
    var dian_material = new THREE.MeshLambertMaterial({ color: 0xff0000 });
    var star = new THREE.Mesh(dian_geometry, dian_material);
    scene.add(star);
    star.position.x = Math.random() * planeSize - (planeSize * .5);
    star.position.y = Math.random() * 40000 + 40000;
    star.position.z = Math.random() * planeSize - (planeSize * .5);
}
for (i = 0; i < 100; i++) {
    var dian_geometry = new THREE.SphereGeometry(1000, 10, 10);
    var dian_material = new THREE.MeshLambertMaterial({ color: 0x0099ff });
    var star = new THREE.Mesh(dian_geometry, dian_material);
    scene.add(star);
    star.position.x = Math.random() * planeSize - (planeSize * .5);
    star.position.y = Math.random() * 40000 + 40000;;
    star.position.z = Math.random() * planeSize - (planeSize * .5);
}
for (i = 0; i < 100; i++) {
    var dian_geometry = new THREE.SphereGeometry(1000, 10, 10);
    var dian_material = new THREE.MeshLambertMaterial({ color: 0x00ff66 });
    var star = new THREE.Mesh(dian_geometry, dian_material);
    scene.add(star);
    star.position.x = Math.random() * planeSize - (planeSize * .5);
    star.position.y = Math.random() * 40000 + 40000;;
    star.position.z = Math.random() * planeSize - (planeSize * .5);
}


//画散点图
var charts = new THREE.Geometry();
for (i = 1; i < 100; i++) {
    var vertex = new THREE.Vector3();//返回沿当前三维线段方向的任意向量
    vertex.x = i * 100 + 10000;
    j = i * 100 + 10000;
    vertex.y = Math.abs(10000 * Math.sin(1000 * j + 100)) + 10000;
    vertex.z = 450000;
    charts.vertices.push(vertex);
}
for (i = 0; i < 100; i++) {
    //datax[i]=10000+i*100;
    var vertex = new THREE.Vector3();
    //vertex.x = datax[i];
    vertex.x = i * 100 + 10000;
    vertex.y = i * 100 + 10000;
    vertex.z = 350000;
    charts.vertices.push(vertex);
}
for (i = 1; i < 100; i++) {
    var vertex = new THREE.Vector3();
    vertex.x = -i * 100 - 10000;
    j = i * 100 + 10000;
    vertex.y = Math.abs(10000 * Math.sin(1000 * j + 100)) + 10000;
    vertex.z = 500000;
    charts.vertices.push(vertex);
}
for (i = 0; i < 100; i++) {
    //datax[i]=10000+i*100;
    var vertex = new THREE.Vector3();//返回沿当前三维线段方向的任意向量
    //vertex.x = datax[i];
    vertex.x = -i * 100 - 10000;
    vertex.y = i * 100 + 10000;
    vertex.z = 400000;
    charts.vertices.push(vertex);
}
var chart_material = new THREE.ParticleBasicMaterial({ size: 1 });
var chart_particles = new THREE.ParticleSystem(charts, material);
scene.add(chart_particles);
//画网格 
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
drawGridRight(10000, 30000, 10000, 30000, 10000, 10000, 450000, 2000, 10);
drawGridRight(10000, 30000, 10000, 30000, 10000, 10000, 350000, 2000, 10);
drawGridLeft(-10000, -30000, 10000, 30000, 10000, -10000, 400000, 2000, 10);
drawGridLeft(-10000, -30000, 10000, 30000, 10000, -10000, 500000, 2000, 10);

drawGridRight(10000, 30000, 10000, 30000, 10000, 10000, 250000, 2000, 10);
drawGridRight(10000, 30000, 10000, 30000, 10000, 10000, 150000, 2000, 10);
drawGridLeft(-10000, -30000, 10000, 30000, 10000, -10000, 200000, 2000, 10);
drawGridLeft(-10000, -30000, 10000, 30000, 10000, -10000, 300000, 2000, 10);
drawGridRight(10000, 30000, 10000, 30000, 10000, 10000, 50000, 2000, 10);
drawGridRight(10000, 30000, 10000, 30000, 10000, 10000, -50000, 2000, 10);
drawGridLeft(-10000, -30000, 10000, 30000, 10000, -10000, 0, 2000, 10);
drawGridLeft(-10000, -30000, 10000, 30000, 10000, -10000, 100000, 2000, 10);

//添加坐标变量
function axisflag(x1, y1, x2, y2, z) {
    var material = new THREE.MeshPhongMaterial({
        color: 0x66ccff,
        specular: 0x66ccff,
        shininess: 0
    });
    var loader = new THREE.FontLoader();
    loader.load('../static/fonts/helvetiker_regular.typeface.json', function (font) {
        var mesh = new THREE.Mesh(new THREE.TextGeometry('time', {
            font: font,
            size: 800,
            height: 800
        }), material);
        mesh.position.set(x1, y1, z);
        scene.add(mesh);
        var mesh = new THREE.Mesh(new THREE.TextGeometry('record', {
            font: font,
            size: 800,
            height: 800
        }), material);
        mesh.position.set(x2, y2, z);
        scene.add(mesh);
    });
}
axisflag(32000, 8000, 6000, 32000, 450000);
axisflag(32000, 8000, 6000, 32000, 350000);
axisflag(-32000, 8000, -6000, 32000, 500000);
axisflag(-32000, 8000, -6000, 32000, 400000);



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
        for (i = 0; i < 10; i++) {
            var x = xstart + interval * i;
            var value = i / 10;
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
            var value = i / 10;
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
axisvalueRight(10000, 10000, 2000, 8000, 8000, 450000);
axisvalueRight(10000, 10000, 2000, 8000, 8000, 350000);
axisvalueLeft(10000, 10000, 2000, -8000, 8000, 400000);
axisvalueLeft(10000, 10000, 2000, -8000, 8000, 500000);


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
arrow(10000, 10000, 30000, 10000, 10000, 30000, 350000, 25000);
arrow(-10000, 10000, -30000, 10000, -10000, 30000, 500000, 25000);
arrow(-10000, 10000, -30000, 10000, -10000, 30000, 400000, 25000);

arrow(10000, 10000, 30000, 10000, 10000, 30000, 250000, 25000);
arrow(10000, 10000, 30000, 10000, 10000, 30000, 150000, 25000);
arrow(-10000, 10000, -30000, 10000, -10000, 30000, 300000, 25000);
arrow(-10000, 10000, -30000, 10000, -10000, 30000, 200000, 25000);
arrow(10000, 10000, 30000, 10000, 10000, 30000, 50000, 25000);
arrow(10000, 10000, 30000, 10000, 10000, 30000, -50000, 25000);
arrow(-10000, 10000, -30000, 10000, -10000, 30000, 100000, 25000);
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