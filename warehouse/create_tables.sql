CREATE TABLE IF NOT EXISTS stock_metrics (
    symbol TEXT,
    window_start TIMESTAMP,
    window_end TIMESTAMP,
    avg_price DOUBLE PRECISION,
    high_price DOUBLE PRECISION,
    low_price DOUBLE PRECISION,
    total_volume BIGINT,
    PRIMARY KEY (symbol, window_start)
);
