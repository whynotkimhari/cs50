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

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int collumn = 0; collumn < width; collumn++)
        {
            float oR = image[row][collumn].rgbtRed;
            float oG = image[row][collumn].rgbtGreen;
            float oB = image[row][collumn].rgbtBlue;
            int sR = round(.393 * oR + .769 * oG + .189 * oB);
            int sG = round(.349 * oR + .686 * oG + .168 * oB);
            int sB = round(.272 * oR + .534 * oG + .131 * oB);
            if (sR > 255)
            {
                sR = 255;
            }
            if (sG > 255)
            {
                sG = 255;
            }
            if (sB > 255)
            {
                sB = 255;
            }

            image[row][collumn].rgbtRed = sR;
            image[row][collumn].rgbtGreen = sG;
            image[row][collumn].rgbtBlue = sB;
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
