PRAGMA encoding = "UTF-8";

DROP TABLE IF EXISTS business_info;

CREATE TABLE "business_info" (
	"id"	INTEGER UNIQUE,
	"first"	TEXT,
	"last"	TEXT,
	"birthday"	TEXT,
	"business_name"	TEXT,
	"business_address"	TEXT,
	"contact"	TEXT,
	"email"	TEXT,
	"state"	TEXT,
	"city"	TEXT,
	"zip"	INTEGER,
	"specialization"	TEXT,
	"ownership"	TEXT,
	"website_link"	TEXT,
	"status"	INTEGER DEFAULT 1,
	"mission_statement"	TEXT,
	"hire"	TEXT,
	"password"	TEXT,
	"rating"	INTEGER,
	PRIMARY KEY("first","last","business_name","rating","hire")
);

drop Table if exists prospect_info;
CREATE TABLE "prospect_info" (
	"first"	TEXT,
	"last"	TEXT,
	"birthday"	TEXT,
	"email"	TEXT,
	"education"	TEXT,
	"state"	TEXT,
	"city"	TEXT,
	"bio"	TEXT,
	"status"	INTEGER,
	"contact"	TEXT,
	"password"	TEXT,
	"website_link"	TEXT
);
