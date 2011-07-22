%define dict_name 	dalf
%define version 	2.4.2
%define release 	1

Name: 			stardict-%dict_name
Version: 		%{version}
Release: 		%mkrel %{release}
Summary: 		Dal's Russian Dictionary
License: 		GPLv2+
URL:			http://xdxf.revdanica.com/down/index.php
Group: 			Text tools
Source0: 		atla02_rus-rus_%dict_name.dict.dz
Source1: 		atla02_rus-rus_%dict_name.idx
Source2: 		atla02_rus-rus_%dict_name.ifo
BuildRoot:		%{_tmppath}/%{name}-%{version}-root
BuildArch: 		noarch
Requires: 		stardict

%description
Dal's Russian Dictionary in stardict format

%install
rm -rf %{buildroot}
install -p -m644 -D %SOURCE0 %{buildroot}%{_datadir}/stardict/dic/%dict_name.dict.dz
install -p -m644 -D %SOURCE1 %{buildroot}%{_datadir}/stardict/dic/%dict_name.idx
install -p -m644 -D %SOURCE2 %{buildroot}%{_datadir}/stardict/dic/%dict_name.ifo

%clean
rm -rf %{buildroot}

%files
%{_datadir}/stardict/dic/%{dict_name}*
