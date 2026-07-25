%define upstream_name    Pod-POM-Web
%define upstream_version 1.27

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Fulltext search for Pod::POM::Web

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/damil/Pod-POM-Web
Source0:	https://cpan.metacpan.org/authors/id/D/DA/DAMI/Pod-POM-Web-%{upstream_version}.tar.gz

BuildRequires:	make
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


