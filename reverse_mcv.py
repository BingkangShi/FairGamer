import numpy as np

def calculate_variance_from_fairmcv(fair_mcv_percentage: float, dimension: int = 1):
    """
    Calculate the corresponding variance (for 1D) or trace (for >1D) from a given FairMCV value.
    
    Args:
        fair_mcv_percentage (float): The FairMCV value as a percentage (0-100).
        dimension (int): The dimension of the original data. Default is 1.
    """
    centroid_norm = 1.0  # Default assumption if not provided
    
    if fair_mcv_percentage <= 0 or fair_mcv_percentage > 100:
        print(f"Error: FairMCV must be > 0 and <= 100. Input: {fair_mcv_percentage}")
        return

    try:
        # Inverse logic:
        # FairMCV = 100 / (1 + ln(1 + MCV))
        # 1 + ln(1 + MCV) = 100 / FairMCV
        # ln(1 + MCV) = (100 / FairMCV) - 1
        # MCV = exp((100 / FairMCV) - 1) - 1
        
        exponent = (100.0 / fair_mcv_percentage) - 1.0
        mcv_value = np.exp(exponent) - 1.0
        
        # MCV = sqrt(trace) / centroid_norm
        # trace = (MCV * centroid_norm)^2
        trace_val = (mcv_value * centroid_norm) ** 2
        
        print(f"--- FairMCV Inverse Calculation ---")
        print(f"Input FairMCV: {fair_mcv_percentage}%")
        print(f"Dimension: {dimension}")
        print(f"MCV Value: {mcv_value:.6f}")
        
        if dimension == 1:
            print(f"Corresponding Variance: {trace_val:.6f}")
        else:
            print(f"Corresponding Trace (Sum of Variances): {trace_val:.6f}")
            
    except Exception as e:
        print(f"Calculation error: {e}")

if __name__ == "__main__":
    # Example usage based on user request "I provide FairMCV value..."
    # The user can modify this call or call the function directly.
    calculate_variance_from_fairmcv(fair_mcv_percentage=82.1, dimension=1)
