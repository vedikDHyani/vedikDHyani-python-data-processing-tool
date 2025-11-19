import pandas as pd
import matplotlib.pyplot as plt


def load_data(path: str) -> pd.DataFrame:
    """Load CSV data into a pandas DataFrame."""
    df = pd.read_csv(path)
    return df


def summarize_data(df: pd.DataFrame) -> None:
    """Print summary statistics for the DataFrame."""
    print("=== Summary Statistics ===")
    print(df.describe())


def calculate_correlation(df: pd.DataFrame) -> float:
    """Return correlation value between value1 and value2."""
    return df["value1"].corr(df["value2"])


def plot_data(df: pd.DataFrame, output_path: str = "plot.png") -> None:
    """Create and save a simple line plot of both series."""
    plt.figure(figsize=(8, 5))
    plt.plot(df["index"], df["value1"], marker="o", label="Value 1")
    plt.plot(df["index"], df["value2"], marker="o", label="Value 2")
    plt.title("Visualization of Data Values")
    plt.xlabel("Index")
    plt.ylabel("Values")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")


def main() -> None:
    df = load_data("data.csv")
    summarize_data(df)

    corr = calculate_correlation(df)
    print(f"\nCorrelation between value1 and value2: {corr:.3f}")

    plot_data(df)


if __name__ == "__main__":
    main()
