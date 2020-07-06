#include "stdafx.h"
#include <opencv2\opencv.hpp>

using namespace cv;
using namespace std;

int main()
{
	// 开始计时
	int start = getTickCount();

	// 读入一张图片
	Mat gSrcImage = imread("lena.jpg");

	// 停止计时
	int end = getTickCount();

	// 单位：s
	double time = (end - start) / getTickFrequency();
	printf("%f", time);

	getchar();
    return 0;	
}