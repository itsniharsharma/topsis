# TOPSIS - Multi-Criteria Decision Analysis Tool

Kindly have a look on PyPI package: https://pypi.org/project/Topsis-Nihar-102303012/1.0.0/

## What is TOPSIS?

**TOPSIS** (Technique for Order Preference by Similarity to Ideal Solution) is a multi-criteria decision-making (MCDM) method that ranks alternatives based on their similarity to an ideal solution. It helps organizations make data-driven decisions when evaluating multiple competing projects or alternatives against various criteria.

---

## TOPSIS Methodology

The algorithm follows a systematic 6-step process:

### Step 1: Data Normalization
Each column value is normalized using vector normalization to convert all attributes into a common scale (0-1):

```
Normalized[i,j] = X[i,j] / √(Σ X[i,j]²)
```

This ensures all criteria are on comparable scales regardless of their original units.

### Step 2: Weighted Normalization
Normalized values are multiplied by their assigned weights to reflect importance:

```
Weighted[i,j] = Normalized[i,j] × Weight[j]
```

**Example:** Weights like "1,1,1,2,1,1" indicate that the 4th criterion is twice as important as others.

### Step 3: Ideal & Worst Solution Identification
For each criterion, determine two reference points:
- **Ideal Best Solution (A+):** Maximum value for beneficial criteria (+), minimum for non-beneficial (-)
- **Ideal Worst Solution (A-):** Minimum value for beneficial (+), maximum for non-beneficial (-)

**Beneficial (+):** Higher values are better (e.g., ROI, Market Potential)
**Non-beneficial (-):** Lower values are better (e.g., Cost, Risk, Payback Time)

### Step 4: Distance Calculation
Calculate Euclidean distances from each alternative to the ideal best and worst solutions:

```
D[i]⁺ = √(Σ (V[i,j] - A[j]⁺)²)
D[i]⁻ = √(Σ (V[i,j] - A[j]⁻)²)
```

### Step 5: TOPSIS Score Calculation
The similarity coefficient to the ideal solution determines the final score:

```
TOPSIS Score[i] = D[i]⁻ / (D[i]⁺ + D[i]⁻)
```

**Score Range:** 0 to 1
- **1.0** = Perfectly ideal solution
- **0.5** = Equally distant from ideal and worst
- **0.0** = Perfectly worst solution

### Step 6: Ranking
Alternatives are ranked based on their TOPSIS scores, where higher scores receive better (lower) rank numbers.

---

## Results Table Analysis

### Top Performing Projects
| Project | Score | Rank | Key Strengths |
|---------|-------|------|---------------|
| CRM_Loyalty_System | 0.726 | **1** | Optimal balance of low cost, strong ROI, and strategic fit |
| AI_Customer_Support | 0.699 | **2** | Strong performance across metrics with manageable cost |
| Premium_Packaging_Upgrade | 0.698 | **3** | Excellent risk-reward balance and low implementation cost |
| Inventory_Automation | 0.667 | **4** | Good ROI with moderate costs and lower risk |
| Subscription_Membership_Model | 0.661 | **5** | Balanced growth potential with reasonable investment |

### Bottom Performing Projects
| Project | Score | Rank | Key Challenges |
|---------|-------|------|-----------------|
| Offline_Experience_Store | 0.240 | **15** | High cost (₹50L) with lower strategic fit and longer payback |
| New_Warehouse_Setup | 0.292 | **14** | High cost with long payback period (20 months) |
| Export_To_UAE_Market | 0.349 | **13** | High initial investment (₹45L) with longer payback |

### Score Distribution
- **Score Range:** 0.240 to 0.726
- **Average Score:** ~0.52
- **Interpretation:** Clear differentiation between projects, with winners offering significantly better value propositions

---

## Input Data Structure

The tool evaluates projects based on 6 key criteria:

1. **InitialCost_Lakhs** (-) | Lower is better
   - Project investment requirement
   
2. **ROI_Percent** (+) | Higher is better
   - Return on investment percentage
   
3. **RiskScore** (-) | Lower is better (1-10 scale)
   - Implementation and market risk
   
4. **Payback_Months** (-) | Lower is better
   - Time to recover initial investment
   
5. **StrategicFit** (+) | Higher is better (1-10 scale)
   - Alignment with business goals
   
6. **MarketPotential** (+) | Higher is better (1-10 scale)
   - Growth and expansion potential

---

## Practical Interpretation

### Why TOPSIS?
This methodology helps you:
- ✅ **Make data-driven decisions** on project prioritization
- ✅ **Quantify trade-offs** between competing objectives (cost vs. benefit)
- ✅ **Compare projects objectively** using a single composite metric
- ✅ **Identify quick wins:** Projects with low cost + high ROI + strategic alignment
- ✅ **Portfolio optimization:** Balance risk and return across multiple initiatives

### Key Insights from Your Results
- **Quick Wins:** CRM_Loyalty_System and Premium_Packaging_Upgrade offer excellent value with low risk
- **Strategic Investments:** AI_Customer_Support and Subscription_Membership_Model balance growth with reasonable investment
- **Avoid Now:** Offline_Experience_Store and New_Warehouse_Setup require high capital with uncertain returns

---

## Installation & Usage

```bash
pip install Topsis-Nihar-102303012
```

### Command Line Usage
```bash
topsis data.csv "1,1,1,2,1,1" "+,+,-,-,+,+" output-result.csv
```

### Parameters
- `data.csv` - Input file with criteria values
- Weights - Importance of each criterion (comma-separated)
- Impacts - Direction of each criterion: `+` (beneficial) or `-` (non-beneficial)
- `output-result.csv` - Output file with TOPSIS scores and rankings

---

## Conclusion

The TOPSIS analysis provides a structured, quantitative approach to portfolio management, helping your organization allocate resources to projects that offer the best combination of financial returns, strategic alignment, and manageable risk.