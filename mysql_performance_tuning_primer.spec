%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	MySQL Performance Tuning Primer Script
Name:		mysql_performance_tuning_primer
Version:	1.4
Release:	%mkrel 0.r2.3
Group:		System/Servers
License:	GPL
URL:		http://www.day32.com/MySQL/
Source0:	http://www.day32.com/MySQL/tuning-primer.sh
Requires:	mysql
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-0.r2.3mdv2011.0
+ Revision: 620425
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.4-0.r2.2mdv2010.0
+ Revision: 430142
- rebuild

* Mon Aug 11 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4-0.r2.1mdv2009.0
+ Revision: 270777
- 1.4-r2

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.3-0.r3.1mdv2008.1
+ Revision: 136612
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 07 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3-0.r3.1mdv2008.0
+ Revision: 59817
- 1.3 r3


* Tue May 02 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2-0r2.1mdk
- new version

* Tue May 02 2006 Oden Eriksson <oeriksson@mandriva.com> 0-1mdk
- initial Mandriva package

