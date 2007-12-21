%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	MySQL Performance Tuning Primer Script
Name:		mysql_performance_tuning_primer
Version:	1.3
Release:	%mkrel 0.r3.1
Group:		System/Servers
License:	GPL
URL:		http://www.day32.com/MySQL/
Source0:	http://www.day32.com/MySQL/tuning-primer.sh
Requires:	mysql
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This script takes information from "SHOW STATUS LIKE..." and "SHOW VARIABLES
LIKE..." to produce sane recomendations for tuning server variables. It is
compatibly with all versions of MySQL 3.23 and higher (including 5.1).
   
 o Currently it handles recomendations for the following:  
 o Slow Query Log 
 o Max Connections 
 o Worker Threads 
 o Key Buffer 
 o Query Cache 
 o Sort Buffer 
 o Joins 
 o Temp Tables 
 o Table (Open & Definition) Cache 
 o Table Locking 
 o Table Scans (read_buffer) 
 o Innodb Status 

%prep

%setup -q -c -T

cp %{SOURCE0} mysql_performance_tuning_primer
perl -pi -e "s|^#\!/.*|#!/bin/bash|g" mysql_performance_tuning_primer

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -m0755 mysql_performance_tuning_primer %{buildroot}%{_sbindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root)
%attr(0755,root,root) %{_sbindir}/mysql_performance_tuning_primer
