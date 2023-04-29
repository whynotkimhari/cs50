#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int collumn = 0; collumn < width; collumn++)
        {
            int k = round((image[row][collumn].rgbtRed + image[row][collumn].rgbtBlue + image[row][collumn].rgbtGreen) / 3.0);
            image[row][collumn].rgbtRed = k;
            image[row][collumn].rgbtBlue = k;
            image[row][collumn].rgbtGreen = k;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
        for (int collumn = 0; collumn < width / 2; collumn++)
        {
            int a = image[row][collumn].rgbtRed;
            int b = image[row][collumn].rgbtGreen;
            int c = image[row][collumn].rgbtBlue;
            image[row][collumn].rgbtRed = image[row][- collumn - 1 + width].rgbtRed;
            image[row][collumn].rgbtGreen = image[row][- collumn - 1 + width].rgbtGreen;
            image[row][collumn].rgbtBlue = image[row][- collumn - 1 + width].rgbtBlue;
            image[row][- collumn - 1 + width].rgbtRed = a;
            image[row][- collumn - 1 + width].rgbtGreen = b;
            image[row][- collumn - 1 + width].rgbtBlue = c;
        }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE trade[height][width];
    for (int row = 0; row < height; row++)
    {
        for (int collumn = 0; collumn < width; collumn++)
        {
            trade[row][collumn] = image[row][collumn];
        }
    }
    //Do at (0;0)
    image[0][0].rgbtRed = round((trade[0][0].rgbtRed + trade[0][1].rgbtRed + trade[1][0].rgbtRed + trade[1][1].rgbtRed) * .25);
    image[0][0].rgbtGreen = round((trade[0][0].rgbtGreen + trade[0][1].rgbtGreen + trade[1][0].rgbtGreen + trade[1][1].rgbtGreen) *
                                  .25);
    image[0][0].rgbtBlue = round((trade[0][0].rgbtBlue + trade[0][1].rgbtBlue + trade[1][0].rgbtBlue + trade[1][1].rgbtBlue) * .25);

    //Do at (0;width-1)
    image[0][width - 1].rgbtRed = round((trade[0][width - 1].rgbtRed + trade[0][width - 2].rgbtRed + trade[1][width - 1].rgbtRed +
                                         trade[1][width - 2].rgbtRed) * .25);
    image[0][width - 1].rgbtGreen = round((trade[0][width - 1].rgbtGreen + trade[0][width - 2].rgbtGreen + trade[1][width - 1].rgbtGreen
                                           + trade[1][width - 2].rgbtGreen) * .25);
    image[0][width - 1].rgbtBlue = round((trade[0][width - 1].rgbtBlue + trade[0][width - 2].rgbtBlue + trade[1][width - 1].rgbtBlue +
                                          trade[1][width - 2].rgbtBlue) * .25);

    //Do at (height-1;0)
    image[height - 1][0].rgbtRed = round((trade[height - 1][0].rgbtRed + trade[height - 2][0].rgbtRed + trade[height - 1][1].rgbtRed +
                                          trade[height - 2][1].rgbtRed) * .25);
    image[height - 1][0].rgbtGreen = round((trade[height - 1][0].rgbtGreen + trade[height - 2][0].rgbtGreen + trade[height -
                                            1][1].rgbtGreen + trade[height - 2][1].rgbtGreen) * .25);
    image[height - 1][0].rgbtBlue = round((trade[height - 1][0].rgbtBlue + trade[height - 2][0].rgbtBlue + trade[height - 1][1].rgbtBlue
                                           + trade[height - 2][1].rgbtBlue) * .25);

    //Do at (height-1;width-1)
    image[height - 1][width - 1].rgbtRed = round((trade[height - 1][width - 1].rgbtRed + trade[height - 2][width - 1].rgbtRed +
                                           trade[height - 1][width - 2].rgbtRed + trade[height - 2][width - 2].rgbtRed) * .25);
    image[height - 1][width - 1].rgbtGreen = round((trade[height - 1][width - 1].rgbtGreen + trade[height - 2][width - 1].rgbtGreen +
            trade[height - 1][width - 2].rgbtGreen + trade[height - 2][width - 2].rgbtGreen) * .25);
    image[height - 1][width - 1].rgbtBlue = round((trade[height - 1][width - 1].rgbtBlue + trade[height - 2][width - 1].rgbtBlue +
                                            trade[height - 1][width - 2].rgbtBlue + trade[height - 2][width - 2].rgbtBlue) * .25);

    for (int row = 0; row < height; row++)
    {
        for (int collumn = 0; collumn < width; collumn++)
        {
            if (row == 0 && (collumn >= 2 && collumn <= width))
            {
                image[0][collumn - 1].rgbtRed = round((trade[0][collumn - 1].rgbtRed + trade[0][collumn - 2].rgbtRed + trade[0][collumn].rgbtRed +
                                                       trade[1][collumn - 1].rgbtRed + trade[1][collumn - 2].rgbtRed + trade[1][collumn].rgbtRed) / 6.0);
                image[0][collumn - 1].rgbtGreen = round((trade[0][collumn - 1].rgbtGreen + trade[0][collumn - 2].rgbtGreen +
                                                        trade[0][collumn].rgbtGreen + trade[1][collumn - 1].rgbtGreen + trade[1][collumn - 2].rgbtGreen + trade[1][collumn].rgbtGreen) /
                                                        6.0);
                image[0][collumn - 1].rgbtBlue = round((trade[0][collumn - 1].rgbtBlue + trade[0][collumn - 2].rgbtBlue + trade[0][collumn].rgbtBlue
                                                        + trade[1][collumn - 1].rgbtBlue + trade[1][collumn - 2].rgbtBlue + trade[1][collumn].rgbtBlue) / 6.0);
            }

            if (row == height - 1 && (collumn >= 2 && collumn <= width))
            {
                image[height - 1][collumn - 1].rgbtRed = round((trade[height - 1][collumn - 1].rgbtRed + trade[height - 1][collumn - 2].rgbtRed +
                        trade[height - 1][collumn].rgbtRed + trade[height - 2][collumn - 1].rgbtRed + trade[height - 2][collumn - 2].rgbtRed + trade[height
                                - 2][collumn].rgbtRed) / 6.0);
                image[height - 1][collumn - 1].rgbtGreen = round((trade[height - 1][collumn - 1].rgbtGreen + trade[height - 1][collumn -
                        2].rgbtGreen + trade[height - 1][collumn].rgbtGreen + trade[height - 2][collumn - 1].rgbtGreen + trade[height - 2][collumn -
                                2].rgbtGreen + trade[height - 2][collumn].rgbtGreen) / 6.0);
                image[height - 1][collumn - 1].rgbtBlue = round((trade[height - 1][collumn - 1].rgbtBlue + trade[height - 1][collumn - 2].rgbtBlue +
                        trade[height - 1][collumn].rgbtBlue + trade[height - 2][collumn - 1].rgbtBlue + trade[height - 2][collumn - 2].rgbtBlue +
                        trade[height - 2][collumn].rgbtBlue) / 6.0);
            }

            if (collumn == 0 && (row >= 2 && row <= height))
            {
                image[row - 1][0].rgbtRed = round((trade[row - 1][0].rgbtRed + trade[row - 2][0].rgbtRed + trade[row][0].rgbtRed + trade[row -
                                                   1][1].rgbtRed + trade[row][1].rgbtRed + trade[row - 2][1].rgbtRed) / 6.0);
                image[row - 1][0].rgbtGreen = round((trade[row - 1][0].rgbtGreen + trade[row - 2][0].rgbtGreen + trade[row][0].rgbtGreen + trade[row
                                                     - 1][1].rgbtGreen + trade[row][1].rgbtGreen + trade[row - 2][1].rgbtGreen) / 6.0);
                image[row - 1][0].rgbtBlue = round((trade[row - 1][0].rgbtBlue + trade[row - 2][0].rgbtBlue + trade[row][0].rgbtBlue + trade[row -
                                                    1][1].rgbtBlue + trade[row][1].rgbtBlue + trade[row - 2][1].rgbtBlue) / 6.0);
            }

            if (collumn == width - 1 && (row >= 2 && row <= height))
            {
                image[row - 1][width - 1].rgbtRed = round((trade[row - 1][width - 1].rgbtRed + trade[row - 2][width - 1].rgbtRed + trade[row][width
                                                    - 1].rgbtRed + trade[row - 1][width - 2].rgbtRed + trade[row][width - 2].rgbtRed + trade[row - 2][width - 2].rgbtRed) / 6.0);
                image[row - 1][width - 1].rgbtGreen = round((trade[row - 1][width - 1].rgbtGreen + trade[row - 2][width - 1].rgbtGreen +
                                                      trade[row][width - 1].rgbtGreen + trade[row - 1][width - 2].rgbtGreen + trade[row][width - 2].rgbtGreen + trade[row - 2][width -
                                                              2].rgbtGreen) / 6.0);
                image[row - 1][width - 1].rgbtBlue = round((trade[row - 1][width - 1].rgbtBlue + trade[row - 2][width - 1].rgbtBlue +
                                                     trade[row][width - 1].rgbtBlue + trade[row - 1][width - 2].rgbtBlue + trade[row][width - 2].rgbtBlue + trade[row - 2][width -
                                                             2].rgbtBlue) / 6.0);
            }

            if (row > 1 && collumn > 1)
            {
                image[row - 1][collumn - 1].rgbtRed = round((trade[row - 1][collumn - 1].rgbtRed + trade[row][collumn - 1].rgbtRed + trade[row -
                                                      2][collumn - 1].rgbtRed + trade[row - 1][collumn].rgbtRed + trade[row - 1][collumn - 2].rgbtRed + trade[row][collumn].rgbtRed +
                                                      trade[row][collumn - 2].rgbtRed + trade[row - 2][collumn].rgbtRed + trade[row - 2][collumn - 2].rgbtRed) / 9.0);
                image[row - 1][collumn - 1].rgbtGreen = round((trade[row - 1][collumn - 1].rgbtGreen + trade[row][collumn - 1].rgbtGreen + trade[row
                                                        - 2][collumn - 1].rgbtGreen + trade[row - 1][collumn].rgbtGreen + trade[row - 1][collumn - 2].rgbtGreen +
                                                        trade[row][collumn].rgbtGreen + trade[row][collumn - 2].rgbtGreen + trade[row - 2][collumn].rgbtGreen + trade[row - 2][collumn -
                                                                2].rgbtGreen) / 9.0);
                image[row - 1][collumn - 1].rgbtBlue = round((trade[row - 1][collumn - 1].rgbtBlue + trade[row][collumn - 1].rgbtBlue + trade[row -
                                                       2][collumn - 1].rgbtBlue + trade[row - 1][collumn].rgbtBlue + trade[row - 1][collumn - 2].rgbtBlue + trade[row][collumn].rgbtBlue +
                                                       trade[row][collumn - 2].rgbtBlue + trade[row - 2][collumn].rgbtBlue + trade[row - 2][collumn - 2].rgbtBlue) / 9.0);
            }
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    //Make a black (000) tmp
    RGBTRIPLE tmp[height + 2][width + 2];
    for (int j = 0; j < height + 2; j++)
    {
        for (int i = 0; i < width + 2; i++)
        {
            tmp[j][i].rgbtRed = 0;
            tmp[j][i].rgbtGreen = 0;
            tmp[j][i].rgbtBlue = 0;
        }
    }
    //Paint image on tmp
    for (int j = 0; j < height; j++)
    {
        for (int i = 0; i < width; i++)
        {
            tmp[j + 1][i + 1] = image[j][i];
        }
    }

    for (int j = 1; j <= height; j++)
    {
        for (int i = 1; i <= width; i++)
        {
            //Gx
            float Gx_Red = tmp[j - 1][i - 1].rgbtRed * (-1) + tmp[j][i - 1].rgbtRed * (-2) + tmp[j + 1][i - 1].rgbtRed *
                           (-1) + tmp[j - 1][i + 1].rgbtRed * (1) + tmp[j][i + 1].rgbtRed * (2) + tmp[j + 1][i + 1].rgbtRed * (1);
            float Gx_Green = tmp[j - 1][i - 1].rgbtGreen * (-1) + tmp[j][i - 1].rgbtGreen * (-2) + tmp[j + 1][i - 1].rgbtGreen *
                             (-1) + tmp[j - 1][i + 1].rgbtGreen * (1) + tmp[j][i + 1].rgbtGreen * (2) + tmp[j + 1][i + 1].rgbtGreen * (1);
            float Gx_Blue = tmp[j - 1][i - 1].rgbtBlue * (-1) + tmp[j][i - 1].rgbtBlue * (-2) + tmp[j + 1][i - 1].rgbtBlue *
                            (-1) + tmp[j - 1][i + 1].rgbtBlue * (1) + tmp[j][i + 1].rgbtBlue * (2) + tmp[j + 1][i + 1].rgbtBlue * (1);

            //Gy
            float Gy_Red = tmp[j - 1][i - 1].rgbtRed * (-1) + tmp[j - 1][i].rgbtRed * (-2) + tmp[j - 1][i + 1].rgbtRed *
                           (-1) + tmp[j + 1][i - 1].rgbtRed * (1) + tmp[j + 1][i].rgbtRed * (2) + tmp[j + 1][i + 1].rgbtRed * (1);
            float Gy_Green = tmp[j - 1][i - 1].rgbtGreen * (-1) + tmp[j - 1][i].rgbtGreen * (-2) + tmp[j - 1][i + 1].rgbtGreen *
                             (-1) + tmp[j + 1][i - 1].rgbtGreen * (1) + tmp[j + 1][i].rgbtGreen * (2) + tmp[j + 1][i + 1].rgbtGreen * (1);
            float Gy_Blue = tmp[j - 1][i - 1].rgbtBlue * (-1) + tmp[j - 1][i].rgbtBlue * (-2) + tmp[j - 1][i + 1].rgbtBlue *
                            (-1) + tmp[j + 1][i - 1].rgbtBlue * (1) + tmp[j + 1][i].rgbtBlue * (2) + tmp[j + 1][i + 1].rgbtBlue * (1);

            //Compute
            float Key_Red = sqrt(pow(Gx_Red, 2) + pow(Gy_Red, 2));
            float Key_Green = sqrt(pow(Gx_Green, 2) + pow(Gy_Green, 2));
            float Key_Blue = sqrt(pow(Gx_Blue, 2) + pow(Gy_Blue, 2));

            //Convert Key to Int
            int K_R = round(Key_Red);
            int K_G = round(Key_Green);
            int K_B = round(Key_Blue);

            //Check if Key (to Int) is valid
            if (K_R > 255)
            {
                K_R = 255;
            }

            if (K_G > 255)
            {
                K_G = 255;
            }

            if (K_B > 255)
            {
                K_B = 255;
            }

            //Return value of K back to image[][]
            image[j - 1][i - 1].rgbtRed = K_R;
            image[j - 1][i - 1].rgbtGreen = K_G;
            image[j - 1][i - 1].rgbtBlue = K_B;
        }
    }
    return;
}
