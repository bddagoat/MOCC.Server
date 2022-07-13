-- PRAGMA encoding = "UTF-8";

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
	"zip"	TEXT,
	"specialization"	TEXT,
	"ownership"	TEXT,
	"website_link"	TEXT,
	"status"	INTEGER DEFAULT 1,
	"mission_statement"	TEXT,
	"hire"	TEXT,
	"password"	TEXT,
	"rating"	INTEGER,
	"profile"	TEXT,
	PRIMARY KEY("first","last","business_name")
);

DROP TABLE IF EXISTS prospect_info;
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
	"website_link"	TEXT,
	"id"	INTEGER UNIQUE,
	"specialization"	TEXT,
	"profile"	TEXT,
	PRIMARY KEY("specialization","first","last")
);

DROP TABLE IF EXISTS artist_producer;
CREATE TABLE "artist_producer" (
	"id"	INTEGER,
	"first"	TEXT,
	"last"	TEXT,
	"email"	TEXT,
	"state"	TEXT,
	"city"	TEXT,
	"status"	INTEGER,
	"contact"	TEXT,
	"password"	TEXT,
	"website_link"	TEXT,
	"portfolio"	TEXT,
	"rating"	INTEGER,
	"genre"	INTEGER,
	"profile"	TEXT,
	PRIMARY KEY("first","last","rating","genre")
);

DROP TABLE IF EXISTS gallery_art;
CREATE TABLE "gallery_art" (
	"name"	TEXT,
	"title"	TEXT,
	"email"	TEXT,
	"category"	TEXT,
	"monetize"	TEXT,
	"picture"	TEXT,
	"description"	TEXT,
	PRIMARY KEY("name","title","category")
);

DROP TABLE IF EXISTS art_media;
CREATE TABLE "art_media" (
	"name"	TEXT,
	"title"	TEXT,
	"category"	TEXT,
	"monetize"	TEXT,
	"file"	TEXT,
	"description"	TEXT,
	PRIMARY KEY("name","category","monetize")
);