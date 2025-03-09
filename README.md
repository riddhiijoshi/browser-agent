# Browser-Agent

## Overview
The **Browser-Agent** verifies the price of a specified product on Myntra by comparing the user-provided price with the actual price listed on the Myntra website. This ensures accuracy in price validation for a given product.

## How It Works
1. The user provides three input parameters:
   - **requirement**: The brand name followed by the product name.
   - **expected_output**: The expected price of the product in INR.
   - **link**: The homepage link of Myntra.
2. The agent fetches the actual price from Myntra.
3. It compares the fetched price with the expected price.
4. Returns a validation result based on the comparison.

## Input Parameters
| Parameter         | Description                                      |
|------------------|--------------------------------------------------|
| **requirement**  | Brand name followed by the product name.        |
| **expected_output** | Expected price in INR for validation.       |
| **link**         | Myntra homepage link.                           |

## Sample Input
```json
{
  "requirement": "Give me the price for The Souled Store Violet Hooded Crop Pullover",
  "expected_output": "949",
  "link": "https://www.myntra.com"
}
```

### Breakdown of Sample Input
- **Brand Name**: The Souled Store  
- **Product Name**: Violet Hooded Crop Pullover  
- **Expected Price**: ₹949  
- **Website**: [Myntra](https://www.myntra.com)

## Expected Output
The agent will return a validation result:
- Successful validation : if expected_output matches the price on Myntra website.
- Failed validation : if expected_output does not match the price on Myntra website.


