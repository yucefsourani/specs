%global debug_package %{nil}
Name:           crunch
Version:        3.6
Release:        1%{?dist}
Summary:        A Wordlist Generator
License:        GPLv2
Group:          System Environment/Base
URL:            https://sourceforge.net/projects/crunch-wordlist/
Source0:        http://downloads.sourceforge.net/project/crunch-wordlist/crunch-wordlist/%{name}-%{version}.tgz
BuildRequires:  glibc-devel(x86-32)


%description
A wordlist generator where you can specify a standard character set 
or a character set you specify and generate all possible combinations 
and permutations.

%prep
%autosetup
sed -i 's/sudo $(shell which install)/$(shell which install)/g' Makefile
sed -i 's/$(INSTALL) -d $(INSTALL_OPTIONS)/$(INSTALL) -d /g' Makefile

%build
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license COPYING
%doc COPYING
%{_bindir}/crunch
%{_datadir}/crunch/*
%{_mandir}/man1/crunch.1*


%changelog
* Tue May  1 2018 yucefsourani <youssef.m.sourani@gmail.com> 36-1
- Initial for fedora 28
