create table if not exists tb_ohlc (
    date text,
    ticker text,
    open real,
    high real,
    low real,
    close real,
    volume real,
    primary key (date, ticker)
);
