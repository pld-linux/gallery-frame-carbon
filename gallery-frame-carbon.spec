%define		_frame		carbon
Summary:	Carbon Frame for Gallery2
Summary(pl.UTF-8):   Ramki Carbon dla Gallery2
Name:		gallery-frame-%{_frame}
Version:	1.0.0
Release:	0.1
License:	GPL
Group:		Applications/Publishing
Source0:	http://www.mincel.com/carbon/g2-frame-%{_frame}-%{version}.zip
# Source0-md5:	9e6223f4b1e156a1145b2dee44e5bdd4
URL:		http://www.mincel.com/carbon/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
Requires:	gallery >= 2.1.0
# Will be needed when modules will be separated to packages
#Requires:	gallery-module-imageframe
Requires:	webapps
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/gallery/modules/imageframe/frames/%{_frame}

%description
I created this image frame for Carbon theme and it is based on Shadow
image frame. If the colors are suitable it can be used for other
themes as well.

%description -l pl.UTF-8
Te ramki zostały stworzone dla motywu Carbon i są oparte na ramkach
Shadow. Mogą być używane także dla innych motywów, o ile kolory
pasują.

%prep
%setup -q -n modules

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}

cd imageframe/frames/%{_frame}
cp -R * $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
