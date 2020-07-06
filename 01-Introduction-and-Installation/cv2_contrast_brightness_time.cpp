#include "stdafx.h"
#include <opencv2\opencv.hpp>

using namespace cv;
using namespace std;

int main()
{
	// 开始计时
	int start = getTickCount();

	// 读入一张图片并调整对比度和亮度
	Mat gSrcImage = imread("lena.jpg");
	Mat gDstImage = Mat::zeros(gSrcImage.size(), gSrcImage.type());

	//1.访问每一个像素的方式
	for (int y = 0; y < gSrcImage.rows; y++)
	{
		for (int x = 0; x < gSrcImage.cols; x++)
		{
			for (int c = 0; c < 3; c++)
			{
				gDstImage.at<Vec3b>(y, x)[c] = saturate_cast<uchar>(0.8 * gSrcImage.at<Vec3b>(y, x)[c] + 80);
			}
		}
	}

	//2.最快速的方式
	//gSrcImage.convertTo(gDstImage, -1, 0.8, 80);

	// 停止计时
	int end = getTickCount();

	// 单位：s
	double time = (end - start) / getTickFrequency();
	printf("%f", time);

	getchar();
	return 0;
}
