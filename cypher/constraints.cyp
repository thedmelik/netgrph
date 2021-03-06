-- Create constraints on DB for consistency and performance
--CREATE Garbage
CREATE CONSTRAINT ON (n:Network) ASSERT n.vrfcidr IS UNIQUE
CREATE CONSTRAINT ON (s:Switch) ASSERT s.name IS UNIQUE
CREATE CONSTRAINT ON (v:VRF) ASSERT v.name IS UNIQUE
CREATE CONSTRAINT ON (v:VLAN) ASSERT v.name IS UNIQUE
CREATE CONSTRAINT ON (e:Entity) ASSERT e.name IS UNIQUE
CREATE INDEX ON :Network(cidr)
CREATE INDEX ON :VLAN(vid)
CREATE INDEX ON :VLAN(mgmt)
