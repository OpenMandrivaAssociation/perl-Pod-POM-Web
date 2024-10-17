%define upstream_name    Pod-POM-Web
%define upstream_version 1.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Fulltext search for Pod::POM::Web

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
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


