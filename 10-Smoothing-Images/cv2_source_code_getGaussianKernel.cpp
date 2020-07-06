cv::Mat cv::getGaussianKernel(int n, double sigma, int ktype)
{
    // 对于常见的卷积核，无需计算，直接查表
    const int SMALL_GAUSSIAN_SIZE = 7;
    static const float small_gaussian_tab[][SMALL_GAUSSIAN_SIZE] =
        {
            {1.f},
            {0.25f, 0.5f, 0.25f},
            {0.0625f, 0.25f, 0.375f, 0.25f, 0.0625f},
            {0.03125f, 0.109375f, 0.21875f, 0.28125f, 0.21875f, 0.109375f, 0.03125f}};

    const float *fixed_kernel = n % 2 == 1 && n <= SMALL_GAUSSIAN_SIZE && sigma <= 0 ? small_gaussian_tab[n >> 1] : 0;

    CV_Assert(ktype == CV_32F || ktype == CV_64F);
    Mat kernel(n, 1, ktype);
    float *cf = kernel.ptr<float>();
    double *cd = kernel.ptr<double>();

    // sigma大于0和小于0两种情况
    double sigmaX = sigma > 0 ? sigma : ((n - 1) * 0.5 - 1) * 0.3 + 0.8;
    double scale2X = -0.5 / (sigmaX * sigmaX);
    double sum = 0;

    int i;
    for (i = 0; i < n; i++)
    {
        double x = i - (n - 1) * 0.5;
        double t = fixed_kernel ? (double)fixed_kernel[i] : std::exp(scale2X * x * x);
        if (ktype == CV_32F)
        {
            cf[i] = (float)t;
            sum += cf[i];
        }
        else
        {
            cd[i] = t;
            sum += cd[i];
        }
    }

    // 计算并乘以缩放系数α
    sum = 1. / sum;
    for (i = 0; i < n; i++)
    {
        if (ktype == CV_32F)
            cf[i] = (float)(cf[i] * sum);
        else
            cd[i] *= sum;
    }

    return kernel;
}
