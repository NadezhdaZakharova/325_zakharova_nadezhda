function setup()
{
	//create a canvas for the robot
	createCanvas(1000, 700);
}

function draw()
{
	strokeWeight(2);

	//robot body 1
	fill(100);
	rect(90, 200, 120, 140);
	rect(60, 200, 50, 100);
	rect(200, 200, 50, 100);
	rect(120, 310, 20, 29);
	rect(160, 310, 20, 29);

	//robot body 2
	fill(200, 730, 80);
  rect(390, 200, 130, 130);
	rect(370, 100, 20, 100);
	rect(520, 200, 80, 20);
	rect(420, 30, 30, 110);
	rect(450, 30, 30, 110);


	//heads

	//robot head 1
	fill(200);
	rect(100, 100, 100, 100, 10);
  fill(200, 330, 450);
    //robot head 2
	rect(400, 100, 100, 100, 10);
   
	//ears
	fill(200, 230, 800);

	//robot ears 1
	rect(93, 130, 10, 33);
	rect(197, 130, 10, 33);

	//robot ears 2
	rect(393, 130, 10, 33);
	rect(497, 130, 10, 33);


	//robots' antennas
	fill(250, 700, 0);
    // robot antenna 1
	ellipse(190, 93, 10, 10);
    // robot antenna 1
	ellipse(410, 93, 10, 10);
    

    //robots' antennas
	fill(200, 0, 200);
    // robot antenna 1
	rect(140, 97, 20, 10);
    // robot antenna 2
	ellipse(450, 30, 20, 10);
    


	//robot 1's eyes
	fill(255);
	ellipse(125, 130, 26, 26);
	point(125, 120);
	ellipse(175, 130, 26, 26);
	point(175, 140);

	//robot 2's eyes
	ellipse(425, 130, 26, 26);
	point(433, 130);
	ellipse(475, 130, 26, 26);
	point(467, 130);


	//robots' noses
	fill(255, 0, 0);
    //robot 1 nose
	triangle(150, 135, 135, 160, 165, 160);
    //robot 2 nose
	triangle(450, 135, 435, 160, 465, 140);
  
	//robot 1 mouth
	noFill();
	beginShape();
	vertex(128, 195);
	vertex(136, 185);
	vertex(142, 195);
	vertex(150, 185);
	vertex(158, 175);
	vertex(166, 185);
	vertex(174, 175);
	endShape();

	//robot 2 mouth
	beginShape();
	vertex(428, 165);
	vertex(436, 185);
	vertex(442, 175);
	vertex(450, 195);
	vertex(458, 175);
	vertex(466, 185);
	vertex(476, 165);
	endShape();
  
  //robot 1's stomach
	fill(200, 30, 80);
	ellipse(155, 260, 86, 66);

	
}