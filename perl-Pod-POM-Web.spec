
%define realname   Pod-POM-Web
%define version    1.11
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Fulltext search for Pod::POM::Web
Source:     http://www.cpan.org/modules/by-module/Pod/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Alien::GvaScript)
BuildRequires: perl(Config)
BuildRequires: perl(Encode::Guess)
BuildRequires: perl(HTTP::Daemon)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(List::Util)
BuildRequires: perl(MIME::Types)
BuildRequires: perl(Module::CoreList)
BuildRequires: perl(POSIX)
BuildRequires: perl(Pod::POM)
BuildRequires: perl(Pod::POM::View::HTML)
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(URI)
BuildRequires: perl(URI::QueryParam)
BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch

%description
the Pod::POM::Web manpage is a Web application for browsing the
documentation of Perl components installed on your local machine. Since
pages are dynamically generated, they are always in sync with code actually
installed.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


