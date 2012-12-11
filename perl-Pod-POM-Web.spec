%define upstream_name    Pod-POM-Web
%define upstream_version 1.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Fulltext search for Pod::POM::Web
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Alien::GvaScript)
BuildRequires:	perl(Config)
BuildRequires:	perl(Encode::Guess)
BuildRequires:	perl(HTTP::Daemon)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(MIME::Types)
BuildRequires:	perl(Module::CoreList)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Pod::POM)
BuildRequires:	perl(Pod::POM::View::HTML)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(URI)
BuildRequires:	perl(URI::QueryParam)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
the Pod::POM::Web manpage is a Web application for browsing the
documentation of Perl components installed on your local machine. Since
pages are dynamically generated, they are always in sync with code actually
installed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.170.0-1mdv2011.0
+ Revision: 662195
- update to new version 1.17

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.150.0-2
+ Revision: 656960
- rebuild for updated spec-helper

* Sun Nov 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.150.0-1mdv2011.0
+ Revision: 602386
- update to new version 1.15

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.140.0-1mdv2011.0
+ Revision: 552603
- update to 1.14

* Mon Jan 18 2010 Jérôme Quelin <jquelin@mandriva.org> 1.130.0-1mdv2010.1
+ Revision: 492954
- update to 1.13

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.110.0-1mdv2010.0
+ Revision: 401615
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.11-2mdv2010.0
+ Revision: 375907
- rebuild

* Tue Mar 31 2009 Jérôme Quelin <jquelin@mandriva.org> 1.11-1mdv2009.1
+ Revision: 362969
- skipping test
- import perl-Pod-POM-Web


* Tue Mar 31 2009 cpan2dist 1.11-1mdv
- initial mdv release, generated with cpan2dist

