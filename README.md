# Browser-Agent

## Overview
The **Browser-Agent** verifies the price of a specified product on Myntra by comparing the user-provided price with the actual price listed on the Myntra website. This ensures accuracy in price validation for a given product.

## How It Works
1. The user provides three input parameters:
   - **requirement**: The brand name followed by the product name.
   - **expected_output**: The expected price range (float) of the product in INR.
   - **link**: The homepage link of Myntra.
2. The agent fetches the actual price from Myntra.
3. It compares the fetched price with the expected price.
4. Returns a validation result based on the comparison.

## Input Parameters
| Parameter         | Description                                      |
|------------------|--------------------------------------------------|
| **requirement**  | Brand name followed by the product name.        |
| **expected_output** | Expected price range (float) in INR for validation.       |
| **link**         | Myntra homepage link.                           |

## Sample Input
```json
{
  "requirement": "Give me the price for The Souled Store Violet Hooded Crop Pullover",
  "expected_output": [900.0, 1000.0],
  "link": "https://www.myntra.com"
}
```

### Breakdown of Sample Input
- **Brand Name**: The Souled Store  
- **Product Name**: Violet Hooded Crop Pullover  
- **Expected Price**: [900.0, 1000.0],
- **Website**: [Myntra](https://www.myntra.com)

## Expected Output
The agent will return a validation result:

- Successful validation and you can make the purchase : if price of product on Myntra is in the price range provided by user .
- Failed validation : if price of product on Myntra is NOT in the price range provided by user .

## Important:
Please make sure you are specifying the brand followed by the exact product name.
example : H&M Shoulder Bag and Pouch
brand : H&M 
product : Shoulder Bag and Pouch
